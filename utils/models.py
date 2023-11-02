mapping_data = {
    # Metadatos de la consulta
    "numero_inmuebles": "consulta_dnprcResult.control.cudnp",
    "numero_unidades_constructivas": "consulta_dnprcResult.control.cucons",
    "tipo_bien_inmueble": "consulta_dnprcResult.bico.bi.idbi.cn",
    "referencia_catastral_1": "consulta_dnprcResult.bico.bi.idbi.rc.pc1",
    "referencia_catastral_2": "consulta_dnprcResult.bico.bi.idbi.rc.pc2",
    "referencia_catastral_cargo": "consulta_dnprcResult.bico.bi.idbi.rc.car",
    "referencia_catastral_digito_1": "consulta_dnprcResult.bico.bi.idbi.rc.cc1",
    "referencia_catastral_digito_2": "consulta_dnprcResult.bico.bi.idbi.rc.cc2",
    # Localizacion del inmueble
    "codigo_provincia_ine": "consulta_dnprcResult.bico.bi.dt.loine.cp",
    "codigo_municipio_ine": "consulta_dnprcResult.bico.bi.dt.loine.cm",
    "codigo_municipio_dgc": "consulta_dnprcResult.bico.bi.dt.cmc",
    "nombre_provincia": "consulta_dnprcResult.bico.bi.dt.np",
    "nombre_municipio": "consulta_dnprcResult.bico.bi.dt.nm",
    "domicilio_tributario": "consulta_dnprcResult.bico.bi.ldt",
    # Localizacion municipal del bien urbano principal y rustico adicional
    "ur_codigo_via": "consulta_dnprcResult.bico.bi.dt.locs.lous.lourb.dir.cv",
    "ur_tipo_via": "consulta_dnprcResult.bico.bi.dt.locs.lous.lourb.dir.tv",
    "ur_nombre_via": "consulta_dnprcResult.bico.bi.dt.locs.lous.lourb.dir.nv",
    "ur_primer_numero_policia": "consulta_dnprcResult.bico.bi.dt.locs.lous.lourb.dir.pnp",
    "ur_segundo_numero_policia": "consulta_dnprcResult.bico.bi.dt.locs.lous.lourb.dir.snp",
    "ur_kilometro": "consulta_dnprcResult.bico.bi.dt.locs.lous.lourb.dir.km",
    "ur_direccion_no_estructurada": "consulta_dnprcResult.bico.bi.dt.locs.lous.lourb.dir.td",
    "ur_bloque": "consulta_dnprcResult.bico.bi.dt.locs.lous.lourb.loint.bq",
    "ur_escalera": "consulta_dnprcResult.bico.bi.dt.locs.lous.lourb.loint.es",
    "ur_planta": "consulta_dnprcResult.bico.bi.dt.locs.lous.lourb.loint.pt",
    "ur_puerta": "consulta_dnprcResult.bico.bi.dt.locs.lous.lourb.loint.pu",
    "ur_distrito_postal": "consulta_dnprcResult.bico.bi.dt.locs.lous.lourb.dp",
    "ur_distrito_municipal": "consulta_dnprcResult.bico.bi.dt.locs.lous.lourb.dm",
    "ur_codigo_municipio_agregado": "consulta_dnprcResult.bico.bi.dt.locs.lous.lorus.cma",
    "ur_codigo_zona_concentracion": "consulta_dnprcResult.bico.bi.dt.locs.lous.lorus.czc",
    "ur_codigo_poligono": "consulta_dnprcResult.bico.bi.dt.locs.lous.lorus.cpp.cpo",
    "ur_codigo_parcela": "consulta_dnprcResult.bico.bi.dt.locs.lous.lorus.cpp.cpa",
    "ur_nombre_paraje": "consulta_dnprcResult.bico.bi.dt.locs.lous.lorus.npa",
    "ur_codigo_paraje": "consulta_dnprcResult.bico.bi.dt.locs.lous.lorus.cpaj",
    # Localizacion municipal del bienes rusticos y urbanos adicionales
    "rus_codigo_via": "consulta_dnprcResult.bico.bi.dt.locs.lors.lourb.dir.cv",
    "rus_tipo_via": "consulta_dnprcResult.bico.bi.dt.locs.lors.lourb.dir.tv",
    "rus_nombre_via": "consulta_dnprcResult.bico.bi.dt.locs.lors.lourb.dir.nv",
    "rus_primer_numero_policia": "consulta_dnprcResult.bico.bi.dt.locs.lors.lourb.dir.pnp",
    "rus_segundo_numero_policia": "consulta_dnprcResult.bico.bi.dt.locs.lors.lourb.dir.snp",
    "rus_kilometro": "consulta_dnprcResult.bico.bi.dt.locs.lors.lourb.dir.km",
    "rus_direccion_no_estructurada": "consulta_dnprcResult.bico.bi.dt.locs.lors.lourb.dir.td",
    "rus_bloque": "consulta_dnprcResult.bico.bi.dt.locs.lors.lourb.loint.bq",
    "rus_escalera": "consulta_dnprcResult.bico.bi.dt.locs.lors.lourb.loint.es",
    "rus_planta": "consulta_dnprcResult.bico.bi.dt.locs.lors.lourb.loint.pt",
    "rus_puerta": "consulta_dnprcResult.bico.bi.dt.locs.lors.lourb.loint.pu",
    "rus_distrito_postal": "consulta_dnprcResult.bico.bi.dt.locs.lors.lourb.dp",
    "rus_distrito_municipal": "consulta_dnprcResult.bico.bi.dt.locs.lors.lourb.dm",
    "rus_codigo_municipio_agregado": "consulta_dnprcResult.bico.bi.dt.locs.lors.lorus.cma",
    "rus_codigo_zona_concentracion": "consulta_dnprcResult.bico.bi.dt.locs.lors.lorus.czc",
    "rus_codigo_poligono": "consulta_dnprcResult.bico.bi.dt.locs.lors.lorus.cpp.cpo",
    "rus_codigo_parcela": "consulta_dnprcResult.bico.bi.dt.locs.lors.lorus.cpp.cpa",
    "rus_nombre_paraje": "consulta_dnprcResult.bico.bi.dt.locs.lors.lorus.npa",
    "rus_codigo_paraje": "consulta_dnprcResult.bico.bi.dt.locs.lors.lorus.cpaj",
    # Datos economicos del inmueble
    "uso_inmueble": "consulta_dnprcResult.bico.bi.debi.luso",
    "superficie_catastral": "consulta_dnprcResult.bico.bi.debi.sfc",
    "coeficiente_participacion": "consulta_dnprcResult.bico.bi.debi.cpt",
    "antiguedad": "consulta_dnprcResult.bico.bi.debi.ant",
    # Unidades constructivas
    "unidades_constructivas": "consulta_dnprcResult.bico.lcons[*].{uso: lcd, tipologia: dvcons.dtip, superficie_catastral: dfcons.stl,bloque: dt.lourb.loint.bq, escalera: dt.lourb.loint.es, planta: dt.lourb.loint.pt, puerta: dt.lourb.loint.pu}",
    # Subparcelas
    "subparcelas": "consulta_dnprcResult.bico.lspr[*].{codigo_subparcela: spr.cspr, superficie_catastral: spr.dspr.ssp, calificacion_catastral: spr.dspr.ccc, clase_cultivo: spr.dspr.dcc, intensidad_productiva: spr.dspr.ip}",
}

mapping_xy = {
    "referencia_catastral_1": "Consulta_CPMRCResult.coordenadas.coord[*].pc.pc1",
    "referencia_catastral_2": "Consulta_CPMRCResult.coordenadas.coord[*].pc.pc2",
    "longitud_x": "Consulta_CPMRCResult.coordenadas.coord[*].geo.xcen",
    "latitud_y": "Consulta_CPMRCResult.coordenadas.coord[*].geo.ycen",
    "sistema_coordenadas": "Consulta_CPMRCResult.coordenadas.coord[*].geo.srs",
    "direccion_completa": "Consulta_CPMRCResult.coordenadas.coord[*].ldt",
}

mapping_provinces = {
    "provincia": "consulta_provincieroResult.provinciero.prov[*].np",
    "codigo_provincia_ine": "consulta_provincieroResult.provinciero.prov[*].cpine",
}

mapping_municipalities = {
    "numero_total_municipios": "consulta_municipieroResult.control.cumun",
    "nombres_municipios": "consulta_municipieroResult.municipiero.muni[*].nm",
    "codigos_ine_municipios": "consulta_municipieroResult.municipiero.muni[*].loine.cm",
    "codigos_catastro_municipios": "consulta_municipieroResult.municipiero.muni[*].locat.cmc",
    "codigos_ine_provincia": "consulta_municipieroResult.municipiero.muni[*].loine.cp",
    "codigos_catastro_provincia": "consulta_municipieroResult.municipiero.muni[*].locat.cd",
}
mapping_streets = {
    "numero_total_vias": "consulta_callejeroResult.control.cuca",
    "codigo_via": "consulta_callejeroResult.callejero.calle[*].dir.cv",
    "tipo_via": "consulta_callejeroResult.callejero.calle[*].dir.tv",
    "nombre_via": "consulta_callejeroResult.callejero.calle[*].dir.nv",
    "codigo_ine_municipio": "consulta_callejeroResult.callejero.calle[*].loine.cm",
    "codigo_ine_provincia": "consulta_callejeroResult.callejero.calle[*].loine.cp",
}
mapping_numbers = {}
