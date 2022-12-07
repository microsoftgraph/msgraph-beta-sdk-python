from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

aggregation_option = lazy_import('msgraph.generated.models.aggregation_option')
collapse_property = lazy_import('msgraph.generated.models.collapse_property')
entity_type = lazy_import('msgraph.generated.models.entity_type')
result_template_option = lazy_import('msgraph.generated.models.result_template_option')
search_alteration_options = lazy_import('msgraph.generated.models.search_alteration_options')
search_query = lazy_import('msgraph.generated.models.search_query')
share_point_one_drive_options = lazy_import('msgraph.generated.models.share_point_one_drive_options')
sort_property = lazy_import('msgraph.generated.models.sort_property')

class SearchRequest(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def aggregation_filters(self,) -> Optional[List[str]]:
        """
        Gets the aggregationFilters property value. Contains one or more filters to obtain search results aggregated and filtered to a specific value of a field. Optional.Build this filter based on a prior search that aggregates by the same field. From the response of the prior search, identify the searchBucket that filters results to the specific value of the field, use the string in its aggregationFilterToken property, and build an aggregation filter string in the format '{field}:/'{aggregationFilterToken}/''. If multiple values for the same field need to be provided, use the strings in its aggregationFilterToken property and build an aggregation filter string in the format '{field}:or(/'{aggregationFilterToken1}/',/'{aggregationFilterToken2}/')'. For example, searching and aggregating drive items by file type returns a searchBucket for the file type docx in the response. You can conveniently use the aggregationFilterToken returned for this searchBucket in a subsequent search query and filter matches down to drive items of the docx file type. Example 1 and example 2 show the actual requests and responses.
        Returns: Optional[List[str]]
        """
        return self._aggregation_filters
    
    @aggregation_filters.setter
    def aggregation_filters(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the aggregationFilters property value. Contains one or more filters to obtain search results aggregated and filtered to a specific value of a field. Optional.Build this filter based on a prior search that aggregates by the same field. From the response of the prior search, identify the searchBucket that filters results to the specific value of the field, use the string in its aggregationFilterToken property, and build an aggregation filter string in the format '{field}:/'{aggregationFilterToken}/''. If multiple values for the same field need to be provided, use the strings in its aggregationFilterToken property and build an aggregation filter string in the format '{field}:or(/'{aggregationFilterToken1}/',/'{aggregationFilterToken2}/')'. For example, searching and aggregating drive items by file type returns a searchBucket for the file type docx in the response. You can conveniently use the aggregationFilterToken returned for this searchBucket in a subsequent search query and filter matches down to drive items of the docx file type. Example 1 and example 2 show the actual requests and responses.
        Args:
            value: Value to set for the aggregationFilters property.
        """
        self._aggregation_filters = value
    
    @property
    def aggregations(self,) -> Optional[List[aggregation_option.AggregationOption]]:
        """
        Gets the aggregations property value. Specifies aggregations (also known as refiners) to be returned alongside search results. Optional.
        Returns: Optional[List[aggregation_option.AggregationOption]]
        """
        return self._aggregations
    
    @aggregations.setter
    def aggregations(self,value: Optional[List[aggregation_option.AggregationOption]] = None) -> None:
        """
        Sets the aggregations property value. Specifies aggregations (also known as refiners) to be returned alongside search results. Optional.
        Args:
            value: Value to set for the aggregations property.
        """
        self._aggregations = value
    
    @property
    def collapse_properties(self,) -> Optional[List[collapse_property.CollapseProperty]]:
        """
        Gets the collapseProperties property value. Contains the ordered collection of fields and limit to collapse results. Optional.
        Returns: Optional[List[collapse_property.CollapseProperty]]
        """
        return self._collapse_properties
    
    @collapse_properties.setter
    def collapse_properties(self,value: Optional[List[collapse_property.CollapseProperty]] = None) -> None:
        """
        Sets the collapseProperties property value. Contains the ordered collection of fields and limit to collapse results. Optional.
        Args:
            value: Value to set for the collapseProperties property.
        """
        self._collapse_properties = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new searchRequest and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Contains one or more filters to obtain search results aggregated and filtered to a specific value of a field. Optional.Build this filter based on a prior search that aggregates by the same field. From the response of the prior search, identify the searchBucket that filters results to the specific value of the field, use the string in its aggregationFilterToken property, and build an aggregation filter string in the format '{field}:/'{aggregationFilterToken}/''. If multiple values for the same field need to be provided, use the strings in its aggregationFilterToken property and build an aggregation filter string in the format '{field}:or(/'{aggregationFilterToken1}/',/'{aggregationFilterToken2}/')'. For example, searching and aggregating drive items by file type returns a searchBucket for the file type docx in the response. You can conveniently use the aggregationFilterToken returned for this searchBucket in a subsequent search query and filter matches down to drive items of the docx file type. Example 1 and example 2 show the actual requests and responses.
        self._aggregation_filters: Optional[List[str]] = None
        # Specifies aggregations (also known as refiners) to be returned alongside search results. Optional.
        self._aggregations: Optional[List[aggregation_option.AggregationOption]] = None
        # Contains the ordered collection of fields and limit to collapse results. Optional.
        self._collapse_properties: Optional[List[collapse_property.CollapseProperty]] = None
        # Contains the connection to be targeted. Respects the following format : /external/connections/connectionid where connectionid is the ConnectionId defined in the Connectors Administration.  Note: contentSource is only applicable when entityType=externalItem. Optional.
        self._content_sources: Optional[List[str]] = None
        # This triggers hybrid sort for messages: the first 3 messages are the most relevant. This property is only applicable to entityType=message. Optional.
        self._enable_top_results: Optional[bool] = None
        # One or more types of resources expected in the response. Possible values are: list, site, listItem, message, event, drive, driveItem, person, externalItem, acronym, bookmark, chatMessage. For details about combinations of two or more entity types that are supported in the same search request, see known limitations. Required.
        self._entity_types: Optional[List[entity_type.EntityType]] = None
        # Contains the fields to be returned for each resource object specified in entityTypes, allowing customization of the fields returned by default otherwise, including additional fields such as custom managed properties from SharePoint and OneDrive, or custom fields in externalItem from content that Microsoft Graph connectors bring in. The fields property can be using the semantic labels applied to properties. For example, if a property is label as title, you can retrieve it using the following syntax : label_title.Optional.
        self._fields: Optional[List[str]] = None
        # Specifies the offset for the search results. Offset 0 returns the very first result. Optional.
        self._from_escaped: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The query property
        self._query: Optional[search_query.SearchQuery] = None
        # Provides query alteration options formatted as a JSON blob that contains two optional flags related to spelling correction. Optional.
        self._query_alteration_options: Optional[search_alteration_options.SearchAlterationOptions] = None
        # Required for searches that use application permissions. Represents the geographic location for the search. For details, see Get the region value.
        self._region: Optional[str] = None
        # Provides the search result templates options for rendering connectors search results.
        self._result_template_options: Optional[result_template_option.ResultTemplateOption] = None
        # Indicates the kind of contents to be searched when a search is performed using application permissions. Optional.
        self._share_point_one_drive_options: Optional[share_point_one_drive_options.SharePointOneDriveOptions] = None
        # The size of the page to be retrieved. Optional.
        self._size: Optional[int] = None
        # Contains the ordered collection of fields and direction to sort results. There can be at most 5 sort properties in the collection. Optional.
        self._sort_properties: Optional[List[sort_property.SortProperty]] = None
        # The stored_fields property
        self._stored_fields: Optional[List[str]] = None
        # Indicates whether to trim away the duplicate SharePoint files from search results. Default value is false. Optional.
        self._trim_duplicates: Optional[bool] = None
    
    @property
    def content_sources(self,) -> Optional[List[str]]:
        """
        Gets the contentSources property value. Contains the connection to be targeted. Respects the following format : /external/connections/connectionid where connectionid is the ConnectionId defined in the Connectors Administration.  Note: contentSource is only applicable when entityType=externalItem. Optional.
        Returns: Optional[List[str]]
        """
        return self._content_sources
    
    @content_sources.setter
    def content_sources(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the contentSources property value. Contains the connection to be targeted. Respects the following format : /external/connections/connectionid where connectionid is the ConnectionId defined in the Connectors Administration.  Note: contentSource is only applicable when entityType=externalItem. Optional.
        Args:
            value: Value to set for the contentSources property.
        """
        self._content_sources = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SearchRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SearchRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SearchRequest()
    
    @property
    def enable_top_results(self,) -> Optional[bool]:
        """
        Gets the enableTopResults property value. This triggers hybrid sort for messages: the first 3 messages are the most relevant. This property is only applicable to entityType=message. Optional.
        Returns: Optional[bool]
        """
        return self._enable_top_results
    
    @enable_top_results.setter
    def enable_top_results(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableTopResults property value. This triggers hybrid sort for messages: the first 3 messages are the most relevant. This property is only applicable to entityType=message. Optional.
        Args:
            value: Value to set for the enableTopResults property.
        """
        self._enable_top_results = value
    
    @property
    def entity_types(self,) -> Optional[List[entity_type.EntityType]]:
        """
        Gets the entityTypes property value. One or more types of resources expected in the response. Possible values are: list, site, listItem, message, event, drive, driveItem, person, externalItem, acronym, bookmark, chatMessage. For details about combinations of two or more entity types that are supported in the same search request, see known limitations. Required.
        Returns: Optional[List[entity_type.EntityType]]
        """
        return self._entity_types
    
    @entity_types.setter
    def entity_types(self,value: Optional[List[entity_type.EntityType]] = None) -> None:
        """
        Sets the entityTypes property value. One or more types of resources expected in the response. Possible values are: list, site, listItem, message, event, drive, driveItem, person, externalItem, acronym, bookmark, chatMessage. For details about combinations of two or more entity types that are supported in the same search request, see known limitations. Required.
        Args:
            value: Value to set for the entityTypes property.
        """
        self._entity_types = value
    
    @property
    def fields(self,) -> Optional[List[str]]:
        """
        Gets the fields property value. Contains the fields to be returned for each resource object specified in entityTypes, allowing customization of the fields returned by default otherwise, including additional fields such as custom managed properties from SharePoint and OneDrive, or custom fields in externalItem from content that Microsoft Graph connectors bring in. The fields property can be using the semantic labels applied to properties. For example, if a property is label as title, you can retrieve it using the following syntax : label_title.Optional.
        Returns: Optional[List[str]]
        """
        return self._fields
    
    @fields.setter
    def fields(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the fields property value. Contains the fields to be returned for each resource object specified in entityTypes, allowing customization of the fields returned by default otherwise, including additional fields such as custom managed properties from SharePoint and OneDrive, or custom fields in externalItem from content that Microsoft Graph connectors bring in. The fields property can be using the semantic labels applied to properties. For example, if a property is label as title, you can retrieve it using the following syntax : label_title.Optional.
        Args:
            value: Value to set for the fields property.
        """
        self._fields = value
    
    @property
    def from_escaped(self,) -> Optional[int]:
        """
        Gets the from property value. Specifies the offset for the search results. Offset 0 returns the very first result. Optional.
        Returns: Optional[int]
        """
        return self._from_escaped
    
    @from_escaped.setter
    def from_escaped(self,value: Optional[int] = None) -> None:
        """
        Sets the from property value. Specifies the offset for the search results. Offset 0 returns the very first result. Optional.
        Args:
            value: Value to set for the from_escaped property.
        """
        self._from_escaped = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "aggregation_filters": lambda n : setattr(self, 'aggregation_filters', n.get_collection_of_primitive_values(str)),
            "aggregations": lambda n : setattr(self, 'aggregations', n.get_collection_of_object_values(aggregation_option.AggregationOption)),
            "collapse_properties": lambda n : setattr(self, 'collapse_properties', n.get_collection_of_object_values(collapse_property.CollapseProperty)),
            "content_sources": lambda n : setattr(self, 'content_sources', n.get_collection_of_primitive_values(str)),
            "enable_top_results": lambda n : setattr(self, 'enable_top_results', n.get_bool_value()),
            "entity_types": lambda n : setattr(self, 'entity_types', n.get_collection_of_enum_values(entity_type.EntityType)),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_primitive_values(str)),
            "from": lambda n : setattr(self, 'from_escaped', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "query": lambda n : setattr(self, 'query', n.get_object_value(search_query.SearchQuery)),
            "query_alteration_options": lambda n : setattr(self, 'query_alteration_options', n.get_object_value(search_alteration_options.SearchAlterationOptions)),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "result_template_options": lambda n : setattr(self, 'result_template_options', n.get_object_value(result_template_option.ResultTemplateOption)),
            "share_point_one_drive_options": lambda n : setattr(self, 'share_point_one_drive_options', n.get_object_value(share_point_one_drive_options.SharePointOneDriveOptions)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "sort_properties": lambda n : setattr(self, 'sort_properties', n.get_collection_of_object_values(sort_property.SortProperty)),
            "stored_fields": lambda n : setattr(self, 'stored_fields', n.get_collection_of_primitive_values(str)),
            "trim_duplicates": lambda n : setattr(self, 'trim_duplicates', n.get_bool_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def query(self,) -> Optional[search_query.SearchQuery]:
        """
        Gets the query property value. The query property
        Returns: Optional[search_query.SearchQuery]
        """
        return self._query
    
    @query.setter
    def query(self,value: Optional[search_query.SearchQuery] = None) -> None:
        """
        Sets the query property value. The query property
        Args:
            value: Value to set for the query property.
        """
        self._query = value
    
    @property
    def query_alteration_options(self,) -> Optional[search_alteration_options.SearchAlterationOptions]:
        """
        Gets the queryAlterationOptions property value. Provides query alteration options formatted as a JSON blob that contains two optional flags related to spelling correction. Optional.
        Returns: Optional[search_alteration_options.SearchAlterationOptions]
        """
        return self._query_alteration_options
    
    @query_alteration_options.setter
    def query_alteration_options(self,value: Optional[search_alteration_options.SearchAlterationOptions] = None) -> None:
        """
        Sets the queryAlterationOptions property value. Provides query alteration options formatted as a JSON blob that contains two optional flags related to spelling correction. Optional.
        Args:
            value: Value to set for the queryAlterationOptions property.
        """
        self._query_alteration_options = value
    
    @property
    def region(self,) -> Optional[str]:
        """
        Gets the region property value. Required for searches that use application permissions. Represents the geographic location for the search. For details, see Get the region value.
        Returns: Optional[str]
        """
        return self._region
    
    @region.setter
    def region(self,value: Optional[str] = None) -> None:
        """
        Sets the region property value. Required for searches that use application permissions. Represents the geographic location for the search. For details, see Get the region value.
        Args:
            value: Value to set for the region property.
        """
        self._region = value
    
    @property
    def result_template_options(self,) -> Optional[result_template_option.ResultTemplateOption]:
        """
        Gets the resultTemplateOptions property value. Provides the search result templates options for rendering connectors search results.
        Returns: Optional[result_template_option.ResultTemplateOption]
        """
        return self._result_template_options
    
    @result_template_options.setter
    def result_template_options(self,value: Optional[result_template_option.ResultTemplateOption] = None) -> None:
        """
        Sets the resultTemplateOptions property value. Provides the search result templates options for rendering connectors search results.
        Args:
            value: Value to set for the resultTemplateOptions property.
        """
        self._result_template_options = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("aggregationFilters", self.aggregation_filters)
        writer.write_collection_of_object_values("aggregations", self.aggregations)
        writer.write_collection_of_object_values("collapseProperties", self.collapse_properties)
        writer.write_collection_of_primitive_values("contentSources", self.content_sources)
        writer.write_bool_value("enableTopResults", self.enable_top_results)
        writer.write_enum_value("entityTypes", self.entity_types)
        writer.write_collection_of_primitive_values("fields", self.fields)
        writer.write_int_value("from", self.from_escaped)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("query", self.query)
        writer.write_object_value("queryAlterationOptions", self.query_alteration_options)
        writer.write_str_value("region", self.region)
        writer.write_object_value("resultTemplateOptions", self.result_template_options)
        writer.write_object_value("sharePointOneDriveOptions", self.share_point_one_drive_options)
        writer.write_int_value("size", self.size)
        writer.write_collection_of_object_values("sortProperties", self.sort_properties)
        writer.write_collection_of_primitive_values("stored_fields", self.stored_fields)
        writer.write_bool_value("trimDuplicates", self.trim_duplicates)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def share_point_one_drive_options(self,) -> Optional[share_point_one_drive_options.SharePointOneDriveOptions]:
        """
        Gets the sharePointOneDriveOptions property value. Indicates the kind of contents to be searched when a search is performed using application permissions. Optional.
        Returns: Optional[share_point_one_drive_options.SharePointOneDriveOptions]
        """
        return self._share_point_one_drive_options
    
    @share_point_one_drive_options.setter
    def share_point_one_drive_options(self,value: Optional[share_point_one_drive_options.SharePointOneDriveOptions] = None) -> None:
        """
        Sets the sharePointOneDriveOptions property value. Indicates the kind of contents to be searched when a search is performed using application permissions. Optional.
        Args:
            value: Value to set for the sharePointOneDriveOptions property.
        """
        self._share_point_one_drive_options = value
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. The size of the page to be retrieved. Optional.
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. The size of the page to be retrieved. Optional.
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    
    @property
    def sort_properties(self,) -> Optional[List[sort_property.SortProperty]]:
        """
        Gets the sortProperties property value. Contains the ordered collection of fields and direction to sort results. There can be at most 5 sort properties in the collection. Optional.
        Returns: Optional[List[sort_property.SortProperty]]
        """
        return self._sort_properties
    
    @sort_properties.setter
    def sort_properties(self,value: Optional[List[sort_property.SortProperty]] = None) -> None:
        """
        Sets the sortProperties property value. Contains the ordered collection of fields and direction to sort results. There can be at most 5 sort properties in the collection. Optional.
        Args:
            value: Value to set for the sortProperties property.
        """
        self._sort_properties = value
    
    @property
    def stored_fields(self,) -> Optional[List[str]]:
        """
        Gets the stored_fields property value. The stored_fields property
        Returns: Optional[List[str]]
        """
        return self._stored_fields
    
    @stored_fields.setter
    def stored_fields(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the stored_fields property value. The stored_fields property
        Args:
            value: Value to set for the stored_fields property.
        """
        self._stored_fields = value
    
    @property
    def trim_duplicates(self,) -> Optional[bool]:
        """
        Gets the trimDuplicates property value. Indicates whether to trim away the duplicate SharePoint files from search results. Default value is false. Optional.
        Returns: Optional[bool]
        """
        return self._trim_duplicates
    
    @trim_duplicates.setter
    def trim_duplicates(self,value: Optional[bool] = None) -> None:
        """
        Sets the trimDuplicates property value. Indicates whether to trim away the duplicate SharePoint files from search results. Default value is false. Optional.
        Args:
            value: Value to set for the trimDuplicates property.
        """
        self._trim_duplicates = value
    

