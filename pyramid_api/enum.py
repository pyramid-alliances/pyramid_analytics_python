from enum import IntEnum

from typing import (
    Any,
    Dict,
    List,
    Optional
)

class AccessType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AccessType.htm
    """
    none = 0
    read = 1
    write = 2
    view = 3
    admin = 4
    

class AdjunctRequestType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AdjunctRequestType.htm
    """
    slicer = 0
    collaboration = 1
    maps = 2
    

class AdminType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AdminType.htm
    """
    none = 0
    domainadmin = 1
    enterpriseadmin = 2
    

class AggregationType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AggregationType.htm
    """
    sum = 0
    avg = 1
    min = 2
    max = 3
    count = 4
    distinct_count = 5
    median = 6
    first_quartile = 7
    third_quartile = 8
    none = 9
    var = 10
    var_p = 11
    stdev = 12
    stdev_p = 13
    sum_of_sqr = 14
    cumulative_time_sum = 15
    first_child = 16
    last_child = 17
    first_non_empty = 18
    last_non_empty = 19
    

class AlertIndicatorType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AlertIndicatorType.htm
    """
    same = 0
    good = 1
    bad = 2
    

class ApiResponseFormat(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ApiResponseFormat.htm
    """
    json = 0
    xml = 1
    csv = 2
    odata = 3
    odata_metadata = 4
    odata_db_level = 5
    

class AssetType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AssetType.htm
    """
    text = 0
    header = 1
    timeasset = 2
    dateasset = 3
    processeddate = 4
    image = 5
    vectorimage = 6
    shape = 7
    jsbutton = 8
    urlbutton = 9
    jumpbutton = 10
    webpage = 11
    infographics = 12
    dynamictext = 13
    tableofcontents = 14
    

class AxisTotalsType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AxisTotalsType.htm
    """
    none = 0
    grand_total = 1
    grand_and_sub_total = 2
    sub_total = 3
    

class AxisType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/AxisType.htm
    """
    columns = 0
    rows = 1
    marks = 2
    filters = 3
    none = 4
    

class CacheMode(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CacheMode.htm
    """
    avoid_cache = 0
    use_cache = 1
    model_default = 2
    

class CalcCategoryType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CalcCategoryType.htm
    """
    general = 0
    time = 1
    

class CalcType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CalcType.htm
    """
    none = 0
    custommember = 1
    customset = 2
    parameter = 3
    customscript = 4
    kpi = 5
    customcolumn = 6
    customvisual = 7
    

class CartesianType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CartesianType.htm
    """
    grid = 0
    chart = 1
    segment = 2
    scatter = 3
    tabular = 4
    raw = 5
    map = 6
    

class ChipCategory(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ChipCategory.htm
    """
    measure = 0
    attribute = 1
    clientcalc = 2
    

class ClashDefaultOption(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ClashDefaultOption.htm
    """
    regular_pie_import = 0
    replace_file = 1
    add_new = 2
    skip = 3
    

class ClientLicenseType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ClientLicenseType.htm
    """
    none = 0
    viewer = 100
    professional = 200
    

class CmsNodeExtraDataType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CmsNodeExtraDataType.htm
    """
    script = 0
    parameter = 1
    calcmodelconnection = 2
    kpi = 3
    customvisual = 4
    elementfunction = 5
    

class CollaborationOpenOptions(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CollaborationOpenOptions.htm
    """
    default = 0
    include_comments = 1
    report_snapshot = 2
    result_snapshot = 3
    

class CollaborationRequestType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CollaborationRequestType.htm
    """
    none = 0
    marks = 1
    threads = 2
    

class ColoringDirection(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ColoringDirection.htm
    """
    bottomup = 0
    topdown = 1
    righttoleft = 2
    lefttoright = 3
    

class ColumnPropertiesType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ColumnPropertiesType.htm
    """
    formatted_value = 0
    additional_values_1 = 1
    additional_values_2 = 2
    additional_values_3 = 3
    additional_values_4 = 4
    prefix = 5
    suffix = 6
    

class ComponentType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ComponentType.htm
    """
    none = 0
    grid = 1
    map = 3
    text = 4
    gauge = 5
    columnchart = 6
    linechart = 7
    areachart = 8
    scatterchart = 10
    bubblechart = 11
    piechart = 12
    combochart_deprecated = 13
    treemap = 14
    stackedcolumnchart = 15
    stacked100columnchart = 16
    barchart = 17
    stacked100barchart = 18
    stackedbarchart = 19
    tabulargrid = 20
    splinechart = 21
    steplinechart = 22
    splineareachart = 23
    steplineareachart = 24
    stackedareachart = 25
    stacked100areachart = 26
    splinestackedareachart = 27
    steplinestackedareachart = 28
    splinestacked100areachart = 29
    steplinestacked100areachart = 30
    doughnutchart = 31
    extendedtabulargrid = 32
    pointchart = 33
    pyramidchart = 34
    funnelchart = 35
    marimekkochart = 36
    circlepacking = 37
    shapemap = 38
    sankeychart = 39
    hierarchicaltreemap = 40
    hierarchicalcirclepacking = 46
    wordcloud = 47
    sunburst = 48
    stockchart = 49
    iciclechart = 50
    customvisual = 51
    legend = 52
    boxandwhisker = 53
    waterfall = 54
    streamsplinechart = 55
    streamstepchart = 56
    streamlinechart = 57
    geoheatmap = 58
    bullet = 59
    lollipopchart = 60
    tornadochart = 61
    radarlinechart = 62
    radarareachart = 63
    radarsmoothlinechart = 64
    radarareasmoothlinechart = 65
    radarpointchart = 66
    scatterlinechart = 67
    scattersplinechart = 68
    

class ConditionConjunctionType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ConditionConjunctionType.htm
    """
    none = 0
    or_ = 1
    and_ = 2
    

class ConditionFormulaType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ConditionFormulaType.htm
    """
    formulavsvalue = 0
    formulavsformula = 1
    formulavslastvalue = 2
    

class ConnectionStringType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ConnectionStringType.htm
    """
    none = 0
    ms_olap = 1
    ms_olap_tabular = 2
    powerpivot = 3
    in_memory = 4
    sqlserver = 5
    mysql = 6
    monetdb = 7
    postgresql = 8
    oracle = 9
    db2 = 10
    teradata = 11
    drill = 12
    pa_imdb = 13
    redshift = 14
    presto = 15
    athena = 16
    bigquery = 17
    hive = 18
    salesforce = 19
    sap_hana = 20
    googleanalytics = 21
    mongodbbicx = 22
    sqlserverazure = 23
    snowflake = 24
    sybase = 25
    firebird = 26
    facebook = 27
    vertica = 28
    twitter = 29
    odbcserver = 30
    sharepoint = 31
    sap_bw = 32
    azureblobstorage = 33
    amazons3storage = 34
    greenplum = 35
    exasol = 36
    memsql = 37
    mariadb = 38
    netezza = 39
    glue = 40
    impala = 41
    azuresynapse = 42
    odbcdirectquery = 43
    as400 = 44
    neo4jcypher = 45
    neo4jbi = 46
    customjdbc = 47
    sparksql = 48
    databricks = 49
    denodo = 50
    

class ContainerType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ContainerType.htm
    """
    none = 0
    datadiscovery = 1
    storyboard = 2
    publisher = 3
    etlflow = 4
    

class ContentItemObject(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ContentItemObject.htm
    """
    asset = 0
    publisher = 1
    storyboard = 2
    calculation = 3
    datadiscovery = 4
    folder = 5
    

class ContentType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ContentType.htm
    """
    none = 0
    asset = 1
    calculation = 2
    datadiscovery = 3
    etlflow = 4
    folder = 5
    publisher = 6
    server = 7
    storyboard = 8
    document = 9
    component = 10
    theme = 11
    prom = 12
    contentview = 13
    kpibandscontainer = 15
    datasource = 16
    

class ContentTypeObject(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ContentTypeObject.htm
    """
    none = 0
    asset = 1
    calculation = 2
    datadiscovery = 3
    etlflow = 4
    folder = 5
    publisher = 6
    storyboard = 8
    

class ConversationType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ConversationType.htm
    """
    default = 0
    todo = 1
    workflow = 2
    

class CubeAuthMethod(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CubeAuthMethod.htm
    """
    effectiveusername = 0
    customdata = 1
    none = 2
    

class CustomFontContentType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CustomFontContentType.htm
    """
    fontstylesheet = 0
    fontfile = 1
    

class CustomSetDiscreteValueType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CustomSetDiscreteValueType.htm
    """
    static = 0
    parameter = 1
    custommember = 2
    evaluationsetfunction = 3
    gridcell = 4
    

class CustomVisualApiVersion(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/CustomVisualApiVersion.htm
    """
    getv1 = 0
    getv2 = 1
    

class DataFlowModelType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DataFlowModelType.htm
    """
    virtualmodel = 0
    tabularmodel = 1
    apachedrill = 2
    inmemorymodel = 3
    inmemorycsvmodel = 4
    

class DataPattern(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DataPattern.htm
    """
    continuous = 0
    discrete = 1
    multicontinuous = 2
    multidiscrete = 3
    discretecontinuous = 4
    conditionalformatting = 5
    

class DateSearchType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DateSearchType.htm
    """
    equals = 0
    before = 1
    after = 2
    between = 3
    

class DateSelectionType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DateSelectionType.htm
    """
    value = 0
    function = 1
    

class DayType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DayType.htm
    """
    specific = 0
    repeated = 1
    

class DeviceType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DeviceType.htm
    """
    none = 0
    desktop = 1
    tablet = 2
    phone = 3
    

class DiscoveryWorkspaceType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DiscoveryWorkspaceType.htm
    """
    classic = 0
    analytic = 1
    compact = 2
    custom = 3
    reverseanalytic = 4
    collapsed = 5
    

class DocumentTypeEnum(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DocumentTypeEnum.htm
    """
    regular = 0
    masterpage = 1
    

class DrillState(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DrillState.htm
    """
    none = 0
    expandable = 1
    collapsible = 2
    

class DropZoneType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DropZoneType.htm
    """
    columns = 0
    rows = 1
    values = 2
    size = 3
    color = 4
    filter = 5
    remove = 6
    dimensions = 7
    measures = 8
    tooltip = 9
    xaxis = 10
    trellisvertical = 11
    trellishorizontal = 12
    categories = 13
    labels = 14
    angle = 15
    yaxis = 16
    details = 17
    geo = 18
    advanceanalytics = 19
    indicator = 20
    additionalvalues = 21
    shape = 22
    motion = 23
    

class DynamicEntityType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/DynamicEntityType.htm
    """
    query = 0
    placeholder = 1
    textfield = 2
    jumptourl = 3
    

class ElementFunctionType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ElementFunctionType.htm
    """
    all = 0
    default = 1
    level = 2
    children = 3
    descendants = 4
    drill_up = 5
    all_descendants = 6
    leaf_descendants = 7
    expand = 8
    collapse = 9
    siblings = 10
    grandparent = 11
    greater_than = 12
    greater_or_equal = 13
    less_than = 14
    less_or_equal = 15
    between = 16
    full_tree = 17
    next_member = 18
    prev_member = 19
    lag = 20
    lead = 21
    parent = 22
    first_child = 23
    last_child = 24
    first_sibling = 25
    last_sibling = 26
    current_member = 27
    all_hierarchy_members = 28
    ancestor = 29
    parallel_period = 30
    ascendants = 31
    singe_date_selection = 32
    wtd = 33
    mtd = 34
    qtd = 35
    ytd = 36
    last = 37
    

class EtlExecutionContextType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/EtlExecutionContextType.htm
    """
    item = 0
    materialized = 1
    

class EvaluationSetFunctionType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/EvaluationSetFunctionType.htm
    """
    getmin = 0
    getmax = 1
    getaverage = 2
    getmedian = 3
    getquartile = 4
    getquintile = 5
    getpercentile = 6
    gettertile = 7
    

class ExcelRenderingType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ExcelRenderingType.htm
    """
    matrixgrid = 0
    flatgrid = 1
    rawgrid = 2
    tabulargrid = 3
    notgrid = 4
    

class ExecutionArea(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ExecutionArea.htm
    """
    semantic = 0
    post_query = 1
    semantic_or_cartesian = 2
    sql = 3
    

class FirstWorkday(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/FirstWorkday.htm
    """
    sunday = 1
    monday = 2
    

class FunctionArgumentType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/FunctionArgumentType.htm
    """
    constant = 0
    element_selection = 1
    date_selection = 2
    

class GeneralExecutionError(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/GeneralExecutionError.htm
    """
    error = 1
    nodatasource = 2
    noaccesstodatasource = 3
    noaccesstoitem = 4
    usererror = 5
    itemdoesnotexists = 6
    

class HideMemberType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/HideMemberType.htm
    """
    never = 0
    when_null = 1
    

class HideShowOption(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/HideShowOption.htm
    """
    hide = 0
    show = 1
    

class HierarchyCategory(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/HierarchyCategory.htm
    """
    none = 0
    date = 1
    geo = 2
    person = 3
    

class HierarchyType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/HierarchyType.htm
    """
    drill_path = 0
    parent_child = 1
    regular = 2
    

class ImageSize(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ImageSize.htm
    """
    none = 0
    landscape = 1
    portrait = 2
    landscapesmall = 3
    portraitsmall = 4
    

class ImageUploadStatus(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ImageUploadStatus.htm
    """
    pending = 0
    successful = 1
    getfailed = 2
    

class InteractionContainerType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/InteractionContainerType.htm
    """
    layoutelement = 0
    slicer = 1
    placeholder = 2
    dynamicurl = 3
    trigger = 4
    

class InteractionType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/InteractionType.htm
    """
    data = 0
    sync = 1
    highlight = 2
    initialselection = 3
    

class ItemType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ItemType.htm
    """
    none = 0
    asset = 1
    server = 2
    document = 3
    container = 4
    folder = 5
    calculation = 6
    prom = 7
    etlflow = 8
    customvisual = 9
    

class JoinType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/JoinType.htm
    """
    inner = 0
    right = 1
    left = 2
    full = 3
    cross = 4
    

class KpiAttributeType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/KpiAttributeType.htm
    """
    value = 0
    target = 1
    status = 2
    trend = 3
    bands = 4
    

class KpiStylesOptions(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/KpiStylesOptions.htm
    """
    balls = 0
    signs = 1
    reversedsigns = 2
    tiles = 3
    shapes = 4
    squares = 5
    lights = 6
    text = 7
    arc = 8
    cylinder = 9
    databars = 10
    dial = 11
    bullet = 12
    circles = 13
    

class LayoutBehaviorType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/LayoutBehaviorType.htm
    """
    tiles = 0
    grid = 1
    freeposition = 2
    splitpanel = 3
    

class LayoutElementContentType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/LayoutElementContentType.htm
    """
    visual = 0
    customvisual = 1
    asset = 2
    slicer = 3
    container = 4
    runtimemenubutton = 5
    runtimenavigationbar = 6
    runtimeclosebutton = 7
    tableofcontents = 8
    discovery = 9
    legend = 10
    tablelayout = 11
    tablayout = 12
    scrollablelayout = 13
    

class LayoutElementLegendPosition(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/LayoutElementLegendPosition.htm
    """
    left = 0
    top = 1
    right = 2
    bottom = 3
    discoverypanels = 4
    off = 5
    

class LdapSearchType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/LdapSearchType.htm
    """
    exact = 0
    start_with = 1
    contains = 2
    

class LicenseStatus(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/LicenseStatus.htm
    """
    valid = 0
    expired = 1
    invalid_signature = 2
    invalid_machine_key = 3
    invalid_license_certificate = 4
    

class MasterPageType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MasterPageType.htm
    """
    cover = 0
    content = 1
    

class MaterializedItemType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MaterializedItemType.htm
    """
    none = 0
    database = 1
    modelingmodel = 2
    server = 3
    machinelearningmodel = 4
    schedule = 5
    model = 6
    output = 7
    

class MaterializedRoleAssignmentType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MaterializedRoleAssignmentType.htm
    """
    usedefaultbehavior = 0
    forcepackageroles = 1
    forceexternalroles = 2
    forceparentroles = 3
    

class MathFunction(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MathFunction.htm
    """
    linear = 0
    logarithmic10 = 1
    logarithmic2 = 2
    exponential = 3
    average = 4
    percentageofmax = 5
    positivenegative = 6
    standarddeviation = 7
    valuequartiles = 8
    rankquartiles = 9
    percentageoftotal = 10
    valuequintiles = 11
    valuetertiles = 12
    rankquintiles = 13
    ranktertiles = 14
    coloringhex = 15
    advanced = 16
    discrete = 17
    staticrange = 18
    value = 19
    valuedual = 20
    rankdual = 21
    percentile = 22
    

class MessagesDisplayType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MessagesDisplayType.htm
    """
    none = 0
    warning = 1
    error = 2
    help = 3
    info = 4
    confirmation = 5
    lineageinfo = 6
    

class MiniatureMode(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MiniatureMode.htm
    """
    auto = 0
    off = 1
    

class MobileApplicationType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MobileApplicationType.htm
    """
    none = 0
    tablet = 1
    phone = 2
    

class MobileDeviceType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MobileDeviceType.htm
    """
    ios = 0
    android = 1
    

class ModelAttributeType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelAttributeType.htm
    """
    model_column = 0
    measure = 1
    custom_measure = 2
    hierarchy = 3
    level = 4
    measure_description = 5
    custom_measure_set = 6
    calculated_measure = 7
    ms_kpi = 8
    ms_kpi_attribute = 9
    parameter_measure = 10
    cross_column = 11
    geo_column = 12
    advanced_analytics_column = 13
    properties = 14
    custom_column = 15
    named_measure_set = 16
    default_measure = 17
    

class ModelParameterOperator(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelParameterOperator.htm
    """
    between = 0
    equal = 1
    greaterequal = 2
    greaterthan = 3
    isnotnull = 4
    isnull = 5
    lessequal = 6
    lessthan = 7
    notequal = 8
    

class ModelTextOption(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelTextOption.htm
    """
    none = 0
    before = 1
    after = 2
    

class ModelingColumnCategories(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelingColumnCategories.htm
    """
    none = 0
    year = 1
    quarter = 2
    month = 3
    weeknumber = 4
    weekday = 5
    dayofmonth = 6
    monthname = 7
    dayname = 8
    time = 9
    date = 10
    datetime = 11
    geocountry = 12
    geostate = 13
    geocounty = 14
    geoother = 15
    geocity = 16
    geozip = 17
    geoaddress = 18
    geocustom = 19
    geolongitude = 20
    geolatitude = 21
    machinelearning = 22
    imageurl = 23
    url = 24
    person = 25
    customgeocategory = 26
    

class ModelingParameterSelectionType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelingParameterSelectionType.htm
    """
    singlevalue = 1
    interval = 2
    range = 3
    

class ModelingTableType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ModelingTableType.htm
    """
    table = 0
    customquerytable = 1
    

class MonthDayType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/MonthDayType.htm
    """
    calendar = 0
    specific = 1
    work = 2
    

class NaturalOrderType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/NaturalOrderType.htm
    """
    alphabetically_asc = 0
    alphabetically_desc = 1
    numeric_asc = 2
    numeric_desc = 3
    other = 4
    key_alphabetically_asc = 5
    key_numeric_asc = 6
    

class OnPeakDayOfWeek(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/OnPeakDayOfWeek.htm
    """
    monday = 1
    tuesday = 2
    wednesday = 3
    thursday = 4
    friday = 5
    saturday = 6
    sunday = 7
    

class OperatorType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/OperatorType.htm
    """
    equals = 0
    greater = 1
    less = 2
    greaterorequal = 3
    lessorequal = 4
    notequal = 5
    between = 6
    

class OsType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/OsType.htm
    """
    windows = 0
    mac = 1
    iphone = 2
    ipad = 3
    androidtablet = 4
    androidmobile = 5
    

class PDFConverterType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PDFConverterType.htm
    """
    phantomjs = 0
    electron = 1
    puppeteer = 2
    wkhtml = 3
    itext = 4
    aspose = 5
    svg2pdf = 6
    none = 7
    

class PanelPosition(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PanelPosition.htm
    """
    top = 0
    bottom = 1
    

class PanelSubTitleType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PanelSubTitleType.htm
    """
    breadcrumbs = 0
    custom = 1
    

class PanelTitleType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PanelTitleType.htm
    """
    auto = 0
    reportname = 1
    custom = 2
    

class PaperType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PaperType.htm
    """
    letter = 0
    a4 = 1
    legal = 2
    tabloid = 3
    a3 = 4
    a5 = 5
    a169 = 6
    a34 = 7
    viewport = 8
    custom = 9
    

class ParentChildOrphanHandlingType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ParentChildOrphanHandlingType.htm
    """
    ignored = 0
    roots = 1
    error = 2
    

class ParentChildRollupType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ParentChildRollupType.htm
    """
    self = 0
    children = 1
    self_and_children = 2
    

class PermissionBitIndex(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PermissionBitIndex.htm
    """
    app_assets = 0
    app_presentation = 1
    app_model = 2
    app_discovery = 3
    app_logic = 4
    app_publish = 5
    mod_add_data_server = 6
    mod_use_machine_learning = 7
    mod_create_scripts = 8
    dis_advanced_analytics = 9
    log_create_formulas = 10
    log_create_scripts = 11
    log_custom_columns = 12
    pub_select_multiple_items = 13
    dis_create_data_source = 14
    log_custom_visuals = 15
    mod_create_post_scripts = 16
    gen_advanced_options = 17
    dis_create_shareable = 18
    pub_allow_smart_publish = 19
    pub_allow_scheduling = 20
    pre_allow_smart_present = 21
    dis_lite_version = 22
    pre_present_lite = 23
    mod_execute_process = 24
    dis_auto_disc = 25
    

class PredefinedItemSaveType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PredefinedItemSaveType.htm
    """
    none = 0
    currentuser = 1
    allusers = 2
    

class PrintingHeaderFooterSectionPosition(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PrintingHeaderFooterSectionPosition.htm
    """
    left = 0
    center = 1
    right = 2
    

class PrintingHeaderFooterType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PrintingHeaderFooterType.htm
    """
    header = 0
    footer = 1
    

class PrintingImageQuality(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PrintingImageQuality.htm
    """
    low = 1
    medium = 2
    high = 3
    

class PrintingJobType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PrintingJobType.htm
    """
    online = 0
    offline = 1
    snapshots = 2
    

class PrintingOnlineJobType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PrintingOnlineJobType.htm
    """
    single = 0
    multiplecms = 1
    multipleopentabs = 2
    

class PrintingOutputType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PrintingOutputType.htm
    """
    pdf = 0
    word = 1
    powerpoint = 2
    excel = 3
    html = 4
    image = 5
    noprinting = 6
    csv = 7
    xml = 8
    json = 9
    png = 10
    odata = 11
    

class PrintingPagingType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PrintingPagingType.htm
    """
    fitallcontrolstopage = 0
    fiteachcontroltopage = 1
    fiteachtilecontainertopage = 2
    

class PrintingType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PrintingType.htm
    """
    currentanalysis = 0
    reportlist = 1
    entirebook = 2
    

class PromDefaultSelectionType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PromDefaultSelectionType.htm
    """
    fixedfirst = 0
    fixedlast = 1
    lastchangedbyuniquename = 2
    byindex = 3
    bydynamicvalue = 4
    elementfunction = 5
    byparameterdefault = 6
    lastchangedbymetadata = 7
    lastchangeddynamicvalue = 8
    nometadata = 9
    dateselection = 10
    

class PromSelectionType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PromSelectionType.htm
    """
    element = 0
    numeric = 1
    value_selection = 2
    string = 3
    

class PropertyFieldType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PropertyFieldType.htm
    """
    alignment = 0
    backgroundcolor = 1
    color = 2
    fontfamily = 3
    fontsize = 4
    fontstyle = 5
    fontweight = 6
    legendposition = 7
    opacity = 8
    padding = 9
    strokewidth = 10
    textanchor = 11
    verticalpadding = 12
    colormapping = 13
    fillopacity = 15
    textdecoration = 16
    mastersstoryboard = 17
    masterspublication = 18
    gridtextanchor = 19
    header = 20
    slicerviewmode = 21
    

class PyramidActionParentContainerType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PyramidActionParentContainerType.htm
    """
    model = 0
    discovery = 1
    storyboard = 2
    publisher = 3
    

class PyramidActionTargetType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PyramidActionTargetType.htm
    """
    report = 0
    dimension = 1
    hierarchy = 2
    cells = 3
    member = 4
    

class PyramidActionType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/PyramidActionType.htm
    """
    jumptourl = 0
    jumptoslide = 1
    interacttotarget = 2
    apicall = 3
    jumptoreport = 4
    msdrillthrough = 5
    combined = 6
    javascript = 7
    jumptotab = 8
    

class QomAxisFilterCalculationType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/QomAxisFilterCalculationType.htm
    """
    raw_value = 0
    z_score = 1
    standard_deviation = 2
    average = 3
    median = 4
    

class QomAxisOrderType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/QomAxisOrderType.htm
    """
    values = 0
    labels = 1
    custom = 2
    inverted_hierarchy = 3
    member_key = 4
    natural = 5
    

class QomSelectionType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/QomSelectionType.htm
    """
    hierarchy = 0
    property = 1
    member_prop = 2
    

class QueryInputSelectionType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/QueryInputSelectionType.htm
    """
    double = 0
    string = 1
    parameter = 2
    

class QueryLanguageState(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/QueryLanguageState.htm
    """
    fixedlanguage = 0
    defaultlanguage = 1
    applicationlanguage = 2
    

class QueryScope(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/QueryScope.htm
    """
    container = 0
    document = 1
    

class RatingSearchType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RatingSearchType.htm
    """
    above = 0
    below = 1
    equal = 2
    

class RecurringType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RecurringType.htm
    """
    hourly = 0
    daily = 1
    weekly = 2
    monthly = 3
    

class ReductionType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ReductionType.htm
    """
    aggregate = 0
    count = 1
    average = 2
    minimum = 3
    maximum = 4
    median = 5
    standard_deviation = 6
    sum = 7
    variance = 8
    variance_p = 9
    standard_deviation_p = 10
    covariance = 11
    covariance_p = 12
    correlation = 13
    percentile = 14
    distinct_count = 15
    

class RequestOrigin(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RequestOrigin.htm
    """
    js_client = 0
    api = 1
    task_engine = 2
    router = 3
    satellite = 4
    ws = 5
    api_resolving = 6
    ai = 7
    sdk_api = 8
    

class RoleAssignmentType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RoleAssignmentType.htm
    """
    usedefaultbehavior = 0
    forcepackageroles = 1
    forceexternalroles = 2
    forceparentfolderroles = 3
    

class RootFolderType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RootFolderType.htm
    """
    private = 0
    public = 1
    group = 2
    oneoff = 3
    privatedummy = 4
    tenantsrootfolderdummy = 5
    tenantdummy = 6
    deletedcontent = 7
    crosstenant = 8
    recent = 9
    favorites = 10
    

class RotationDirection(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/RotationDirection.htm
    """
    clockwise = 0
    counterclockwise = 1
    

class ScaleMode(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ScaleMode.htm
    """
    none = 0
    scale = 1
    scalewhenshrinkonly = 2
    shrinktofit = 3
    

class ScheduleDataType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ScheduleDataType.htm
    """
    once = 0
    recurring = 1
    run_once = 2
    

class ScheduleResultType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ScheduleResultType.htm
    """
    none = 0
    containerid = 1
    path = 2
    rendereddata = 3
    flowitemid = 4
    alertcontent = 5
    filedeleted = 6
    

class ScheduleStatus(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ScheduleStatus.htm
    """
    idle = 0
    stopped = 1
    finished = 2
    deleted = 3
    hold = 4
    canceled = 5
    

class ScheduleType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ScheduleType.htm
    """
    printing = 0
    etl = 1
    machine_learning = 2
    user_groups = 3
    logs_clean = 4
    provision = 5
    recommendation = 6
    image_snapshot = 7
    alert = 8
    clean_db = 9
    upgrade_hierarchy_security = 10
    image_snapshot_now = 11
    print_etl = 12
    subscription = 13
    schedules_cleaner = 14
    clean_presentation_documents = 15
    upgrade_te_outputs = 16
    upgrade_content_snapshot_results = 17
    update_private_roles = 18
    

class ScheduleViewType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ScheduleViewType.htm
    """
    none = 0
    basic = 1
    advanced = 2
    

class ScriptType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ScriptType.htm
    """
    bat = 0
    c = 1
    coffeescript = 2
    cpp = 3
    csharp = 4
    dockerfile = 5
    fsharp = 6
    go = 7
    handlebars = 8
    ini = 9
    jade = 10
    java = 11
    javascript = 12
    php = 13
    plaintext = 14
    powershell = 15
    python = 16
    r = 17
    ruby = 18
    sql = 19
    typescript = 20
    sas = 21
    less = 22
    mssql = 23
    pgsql = 24
    mysql = 25
    mdx = 26
    pql = 27
    html = 28
    css = 29
    

class SearchMatchType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SearchMatchType.htm
    """
    contains = 0
    notcontains = 1
    equals = 2
    startswith = 3
    endswith = 4
    

class SearchRootFolderType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SearchRootFolderType.htm
    """
    private = 0
    public = 1
    group = 2
    oneoff = 3
    deletedcontent = 4
    crosstenant = 5
    recent = 6
    favorites = 7
    

class SectionType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SectionType.htm
    """
    general = 0
    grid = 1
    gridcolumnheader = 2
    gridcolormapping = 3
    gridgeneral = 13
    gridmatrixborder = 14
    gridmatrixcolumns = 15
    gridmatrixdata = 17
    gridmatrixrows = 18
    gridrowheader = 19
    visuals = 20
    visualscartesianstyle = 21
    visualsdatalabels = 22
    visualsdatapoints = 23
    visualsgeneral = 24
    visualslegend = 25
    visualsmulticharttitle = 26
    visualsplotarea = 28
    visualsreporttitle = 29
    visualsxaxis = 30
    visualsxaxistitle = 31
    visualsxgridlines = 32
    visualsyaxis = 33
    visualsyaxistitle = 34
    visualsygridlines = 35
    style = 36
    stylegeneral = 37
    styleheading1 = 38
    styleheading2 = 39
    styleheading3 = 40
    styleheading4 = 41
    masters = 43
    mastersstoryboard = 44
    masterspublication = 45
    visualsxtrellisaxis = 46
    visualsytrellisaxis = 47
    visualskpigauges = 48
    panelheader = 49
    panelbreadcrumbs = 50
    slicers = 51
    slicersgeneral = 52
    slicerstitle = 53
    slicersitems = 54
    

class SecurityType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SecurityType.htm
    """
    active_directory = 0
    apache_directory = 1
    open_ldap = 2
    local_os = 3
    azure_active_directory = 4
    saml = 5
    openid_connect = 6
    

class SelectionMethod(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SelectionMethod.htm
    """
    allitems = 0
    firstitem = 1
    lastitem = 2
    custom = 3
    

class ServerAuthenticationMethod(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ServerAuthenticationMethod.htm
    """
    userpassword = 0
    globalactivedirectory = 1
    specificactivedirectory = 2
    serviceaccount = 3
    enduser = 4
    defaultawscredentialsproviderchain = 5
    keytab = 6
    snc = 7
    sap_logon_ticket = 8
    saml = 9
    sharepointapponly = 10
    sap_logon_ticket_custom_data = 11
    

class SimpleAdvancedOptions(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SimpleAdvancedOptions.htm
    """
    simple = 0
    advanced = 1
    

class SlicerMemberDataType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SlicerMemberDataType.htm
    """
    uniquename = 0
    caption = 1
    

class SlicerSearchType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SlicerSearchType.htm
    """
    contains = 0
    notcontains = 1
    equals = 2
    startswith = 3
    endswith = 4
    

class SlicerSelectionMode(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SlicerSelectionMode.htm
    """
    singleselect = 0
    multiselect = 1
    

class SyntaxType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/SyntaxType.htm
    """
    pql = 0
    ms = 1
    bw = 2
    

class TabAppearanceType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TabAppearanceType.htm
    """
    text = 0
    icon = 1
    iconandtext = 2
    

class TabPosition(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TabPosition.htm
    """
    left = 0
    top = 1
    right = 2
    bottom = 3
    off = 4
    

class TagType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TagType.htm
    """
    content = 0
    collaboration = 1
    

class TaskStatus(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TaskStatus.htm
    """
    pending = 0
    finished = 1
    finished_rendering = 2
    error = 3
    running = 4
    finished_with_errors = 5
    stopped_without_running = 6
    during_lock = 7
    canceled = 8
    canceling = 9
    pending_for_evaluation = 10
    during_lock_evaluation = 11
    running_evaluation = 12
    stopped_after_evaluation = 13
    evaluation_canceled = 14
    deleted = 15
    

class TextFieldType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TextFieldType.htm
    """
    currentdate = 0
    creationdate = 1
    modifieddate = 2
    title = 3
    slidetitle = 4
    description = 5
    pagenumber = 6
    createdby = 7
    modifiedby = 8
    totalpages = 9
    modelprocesseddate = 10
    

class ThemeType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ThemeType.htm
    """
    general = 0
    grid = 1
    visuals = 2
    presentation = 3
    publication = 4
    style = 5
    masters = 6
    slicers = 7
    

class ThreadType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ThreadType.htm
    """
    component = 0
    member = 1
    cell = 2
    document = 3
    

class TitlePosition(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/TitlePosition.htm
    """
    vertical = 0
    horizontal = 1
    hide = 2
    

class UserStatusID(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/UserStatusID.htm
    """
    disabled = 0
    enabled = 1
    

class ValidRootFolderType(IntEnum):#
    """ 
    generated from  https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/definitions/ValidRootFolderType.htm
    """
    private = 0
    public = 1
    group = 2
    
