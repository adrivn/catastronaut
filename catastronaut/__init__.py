import json
from itertools import zip_longest
from typing import Self

import jmespath
import polars as pl
import requests as req

from utils.models import (
    mapping_data,
    mapping_municipalities,
    mapping_provinces,
    mapping_streets,
    mapping_xy,
)


class CatastroRetriever:
    baseurl_data: (
        str
    ) = "http://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/"
    baseurl_codes: str = "http://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejeroCodigos.svc/json/"
    baseurl_xy: str = "http://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCoordenadas.svc/json/"
    mapping_data: dict = mapping_data
    mapping_xy: dict = mapping_xy
    mapping_provinces: dict = mapping_provinces
    _result_single: dict = {}
    _result_multiple: list = []
    _temp_single: dict = {}
    _temp_multiple: list = []
    _multiple: bool = False

    @classmethod
    def obtener_datos_geo(
        cls,
        rc: str | list,
        municipio: str | list = "",
        provincia: str | list = "",
        gmaps: bool = True,
    ) -> Self:
        """Devuelve las coordenadas geográficas de la finca buscada, en el sistema de coordenadas EPSG4326 (como Google Maps, latitud y longitud), así como la dirección completa de catastro.

        Parametros:
        rc (str): Referencia Catastral. Si supera los 14 caracteres, será truncada a 14 (la búsqueda se realiza por finca matriz, que sólo usa las 14 primeros caracteres)
        municipio (str): Municipio de la finca (parámetro opcional)
        provincia (str): Provincia de la finca (parámetro opcional)
        gmaps (bool): True o False, por defecto True, determina si las coordenadas devueltas son en formato Google Maps (x, y) en lugar del que aparezca por defecto en Catastro

        Devuelve:
        dict: diccionario/objeto JSON con 1) referencias catastrales usadas para la peticion, larga y corta 2) latitud 3) longitud 4) sistema de coordenadas y 5) direccion completa
        """
        cls._multiple = True
        all_params_strings = all(isinstance(x, str) for x in [rc, municipio, provincia])
        all_params_list = all(isinstance(x, list) for x in [rc, municipio, provincia])

        if not all_params_strings or all_params_list:
            if municipio == "" and provincia == "":
                print(
                    "No se ha introducido provincia ni municipio, se realizaran las peticiones unicamente con la(s) referencias catastrales"
                )
            else:
                raise TypeError(
                    "Los parametros deben ser bien texto (strings) o listas de texto (list[str])"
                )

        if all_params_strings:
            rc, municipio, provincia = [rc], [municipio], [provincia]

        compactador_parametros = zip_longest(rc, municipio, provincia, fillvalue="")

        for i_rc, i_mun, i_prov in compactador_parametros:
            parametros = {
                "Provincia": i_prov,
                "Municipio": i_mun,
                "RefCat": i_rc[:14],
                "SRS": "EPSG:4326" if gmaps else None,
            }
            try:
                datos = req.get(cls.baseurl_xy + "Consulta_CPMRC", params=parametros)
                datos.raise_for_status()

                mapped_response = {
                    field_label: jmespath.search(
                        jmespath_expression, json.loads(datos.text)
                    ).pop()
                    if len(jmespath.search(jmespath_expression, json.loads(datos.text)))
                    == 1
                    else jmespath.search(jmespath_expression, json.loads(datos.text))
                    for field_label, jmespath_expression in mapping_xy.items()
                }
                result = {
                    key: val for key, val in mapped_response.items() if val is not None
                }  # en el evento de una peticion incorrecta (referencia catastral mal formada, etc.)
                cls._result_multiple.append(result)

            except req.RequestException as e:
                print(f"Request failed with {e}. Retrying...")
                raise

        return cls

    @classmethod
    def obtener_provincias(cls) -> Self:
        """Devuelve los nombres de todas las provincias para las cuales hay datos del catastro y sus codigos de INE correspondientes

        Parametros:
        separados (bool): Determina si las provincias y codigos deben devolverse separados, en listas independientes, o juntos en una lista de tuplas

        Devuelve:
        dict: diccionario/objeto JSON con 1) número de provincias 2) nombres de provincias y 3) códigos de INE.
        """
        cls._multiple = False
        try:
            datos = req.get(
                "http://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerProvincias"
            )
            datos.raise_for_status()

            mapped_response = {
                field_label: jmespath.search(
                    jmespath_expression, json.loads(datos.text)
                )
                for field_label, jmespath_expression in mapping_provinces.items()
            }
            cls._result_single = {
                key: val for key, val in mapped_response.items() if val is not None
            }  # en el evento de una peticion incorrecta (referencia catastral mal formada, etc.)
            return cls

        except req.RequestException as e:
            print(f"Request failed with {e}. Retrying...")
            raise

    @classmethod
    def obtener_municipios(cls, provincia: str | list) -> Self:
        """Devuelve los nombres de todos los municipios de la provincia solicitada, asi como sus codigos INE y de catastro correspondientes.

        Parametros:
        provincia (str): La provincia, en formato textual, de acuerdo con el nombrado del catastro (en caso de duda, invocar metodo 'obtener_provincias'). Ejemplo: "ALMERIA".

        Devuelve:
        dict: diccionario/objeto JSON con 1) número de municipios 2) nombres de municipios y 3) códigos de INE y DGC.
        """
        cls._multiple = True
        all_params_strings = isinstance(provincia, str)
        all_params_list = all(
            isinstance(p, str) for p in provincia if isinstance(provincia, list)
        )
        if not (all_params_strings or all_params_list):
            raise TypeError("`provincia` solo admite texto o lista de texto.")

        if all_params_strings:
            provincia = [provincia]

        for prov in provincia:
            parametros = {
                "Provincia": prov,
            }

            try:
                print(f"Solicitando municipios de {prov}")
                datos = req.get(
                    "http://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerMunicipios",
                    params=parametros,
                )
                datos.raise_for_status()

                mapped_response = {
                    field_label: jmespath.search(
                        jmespath_expression, json.loads(datos.text)
                    )
                    for field_label, jmespath_expression in mapping_municipalities.items()
                }
                cleaned_response = {
                    key: val for key, val in mapped_response.items() if val is not None
                }  # en el evento de una peticion incorrecta (referencia catastral mal formada, etc.)
                any_vector = mapped_response.popitem()[1]
                cleaned_response |= {"provincia": [prov for _ in any_vector]}
                cls._result_multiple.append(
                    {
                        key: val
                        for key, val in cleaned_response.items()
                        if val is not None
                    }  # en el evento de una peticion incorrecta (referencia catastral mal formada, etc.)
                )
            except req.RequestException as e:
                print(f"Request failed with {e}. Retrying...")
                raise

        return cls

    @classmethod
    def obtener_callejero(cls, provincia: str | list, municipio: str | list) -> Self:
        """Devuelve los nombres de todas las vias, caminos y calles del municipio y de provincia.

        Parametros:
        provincia (str): La provincia, en formato textual, de acuerdo con el nombrado del catastro (en caso de duda, invocar metodo 'obtener_provincias'). Ejemplo: "ALMERIA".
        municipio (str): El municipio, en formato textual, de acuerdo con el nombrado del catastro (en caso de duda, invocar metodo 'obtener_municipios'). Ejemplo: "ADRA".

        Devuelve:
        dict: diccionario/objeto JSON con 1) número de municipios 2) nombres de municipios y 3) códigos de INE y DGC.
        """
        cls._multiple = True

        all_params_strings = all(isinstance(x, str) for x in [municipio, provincia])
        all_params_list = all(isinstance(x, list) for x in [municipio, provincia])

        if not all_params_strings or all_params_list:
            raise TypeError(
                "Los parametros deben ser bien texto (strings) o listas de texto (list[str])"
            )

        if all_params_strings:
            municipio, provincia = [municipio], [provincia]

        compactador_parametros = zip_longest(municipio, provincia, fillvalue="")

        for i_mun, i_prov in compactador_parametros:
            parametros = {
                "Provincia": i_prov,
                "Municipio": i_mun,
            }

            try:
                datos = req.get(
                    "http://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerCallejero",
                    params=parametros,
                )
                datos.raise_for_status()

                mapped_response = {
                    field_label: jmespath.search(
                        jmespath_expression, json.loads(datos.text)
                    )
                    for field_label, jmespath_expression in mapping_streets.items()
                }
                cleaned_response = {
                    key: val for key, val in mapped_response.items() if val is not None
                }  # en el evento de una peticion incorrecta (referencia catastral mal formada, etc.)
                longest_series = mapped_response.popitem()[1]
                cleaned_response |= {
                    "provincia": [i_prov for _ in longest_series],
                    "municipio": [i_mun for _ in longest_series],
                }
                cls._temp_multiple.append(cleaned_response)

            except req.RequestException as e:
                print(f"Request failed with {e}. Retrying...")
                raise

        cls._result_multiple = cls._temp_multiple.copy()
        cls._temp_multiple.clear()
        return cls

    @classmethod
    def obtener_datos_finca(
        cls, rc: str | list, municipio: str | list = "", provincia: str | list = ""
    ) -> dict:
        """Devuelve los datos catastrales no protegidos de la finca buscada.

        Parametros:
        rc (str): Referencia Catastral. Si supera los 14 caracteres, será truncada a 14 (la búsqueda se realiza por finca matriz, que sólo usa las 14 primeros caracteres)
        municipio (str): Municipio de la finca (parámetro opcional)
        provincia (str): Provincia de la finca (parámetro opcional)

        Devuelve:
        dict: diccionario/objeto JSON con 1) referencias catastrales usadas para la peticion, larga y corta 2) datos no protegidos
        """
        cls._multiple = True
        all_params_strings = all(isinstance(x, str) for x in [rc, municipio, provincia])
        all_params_list = all(isinstance(x, list) for x in [rc, municipio, provincia])

        if not all_params_strings or all_params_list:
            if municipio == "" and provincia == "":
                print(
                    "No se ha introducido provincia ni municipio, se realizaran las peticiones unicamente con la(s) referencias catastrales"
                )
            else:
                raise TypeError(
                    "Los parametros deben ser bien texto (strings) o listas de texto (list[str])"
                )

        if all_params_strings:
            rc, municipio, provincia = [rc], [municipio], [provincia]

        compactador_parametros = zip_longest(rc, municipio, provincia, fillvalue="")

        for i_rc, i_mun, i_prov in compactador_parametros:
            parametros = {
                "Provincia": i_rc,
                "Municipio": i_mun,
                "RefCat": i_prov,
            }

            try:
                datos = req.get(cls.baseurl_data + "Consulta_DNPRC", params=parametros)
                datos.raise_for_status()
                # TODO: Incluir un diccionario JMESPath de errores, para determinar lo que sucede
                mapped_response = {
                    field_label: jmespath.search(
                        jmespath_expression, json.loads(datos.text)
                    )
                    for field_label, jmespath_expression in mapping_data.items()
                }
                # Remove keys with None values
                result = {
                    key: val for key, val in mapped_response.items() if val is not None
                }  # en el evento de una peticion incorrecta (referencia catastral mal formada, etc.)
                cls._result_multiple.append(result)

            except req.RequestException as e:
                print(f"Request failed with {e}. Retrying...")
                raise

        return cls

    @classmethod
    def spit(cls) -> dict | list:
        if cls._multiple:
            return cls._result_multiple
        else:
            return cls._result_single

    @classmethod
    def traverse(cls, expression: str) -> Self:
        match cls._multiple:
            case True:
                temp_traverse = [
                    jmespath.search(expression, item) for item in cls._result_multiple
                ]
                cls._result_multiple = temp_traverse
            case _:
                cls._result_single = jmespath.search(expression, cls._result_single)
        return cls

    @classmethod
    def to_dataframe(cls) -> pl.DataFrame:
        if cls._multiple:
            print("Concatenating and writing to Polars DataFrame...")
            return pl.concat([pl.from_dict(d) for d in cls._result_multiple])
        else:
            print("Writing to Polars DataFrame...")
            return pl.from_dict(cls._result_single)
