from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import aggregation_option, collapse_property, entity_type, result_template_option, search_alteration_options, search_query, share_point_one_drive_options, sort_property

@dataclass
class SearchRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Contains one or more filters to obtain search results aggregated and filtered to a specific value of a field. Optional.Build this filter based on a prior search that aggregates by the same field. From the response of the prior search, identify the searchBucket that filters results to the specific value of the field, use the string in its aggregationFilterToken property, and build an aggregation filter string in the format '{field}:/'{aggregationFilterToken}/''. If multiple values for the same field need to be provided, use the strings in its aggregationFilterToken property and build an aggregation filter string in the format '{field}:or(/'{aggregationFilterToken1}/',/'{aggregationFilterToken2}/')'. For example, searching and aggregating drive items by file type returns a searchBucket for the file type docx in the response. You can conveniently use the aggregationFilterToken returned for this searchBucket in a subsequent search query and filter matches down to drive items of the docx file type. Example 1 and example 2 show the actual requests and responses.
    aggregation_filters: Optional[List[str]] = None
    # Specifies aggregations (also known as refiners) to be returned alongside search results. Optional.
    aggregations: Optional[List[aggregation_option.AggregationOption]] = None
    # Contains the ordered collection of fields and limit to collapse results. Optional.
    collapse_properties: Optional[List[collapse_property.CollapseProperty]] = None
    # Contains the connection to be targeted. Respects the following format : /external/connections/connectionid where connectionid is the ConnectionId defined in the Connectors Administration.  Note: contentSource is only applicable when entityType=externalItem. Optional.
    content_sources: Optional[List[str]] = None
    # This triggers hybrid sort for messages: the first 3 messages are the most relevant. This property is only applicable to entityType=message. Optional.
    enable_top_results: Optional[bool] = None
    # One or more types of resources expected in the response. Possible values are: list, site, listItem, message, event, drive, driveItem, person, externalItem, acronym, bookmark, chatMessage. For details about combinations of two or more entity types that are supported in the same search request, see known limitations. Required.
    entity_types: Optional[List[entity_type.EntityType]] = None
    # Contains the fields to be returned for each resource object specified in entityTypes, allowing customization of the fields returned by default otherwise, including additional fields such as custom managed properties from SharePoint and OneDrive, or custom fields in externalItem from content that Microsoft Graph connectors bring in. The fields property can be using the semantic labels applied to properties. For example, if a property is label as title, you can retrieve it using the following syntax : label_title.Optional.
    fields: Optional[List[str]] = None
    # Specifies the offset for the search results. Offset 0 returns the very first result. Optional.
    from_: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The query property
    query: Optional[search_query.SearchQuery] = None
    # Provides query alteration options formatted as a JSON blob that contains two optional flags related to spelling correction. Optional.
    query_alteration_options: Optional[search_alteration_options.SearchAlterationOptions] = None
    # Required for searches that use application permissions. Represents the geographic location for the search. For details, see Get the region value.
    region: Optional[str] = None
    # Provides the search result templates options for rendering connectors search results.
    result_template_options: Optional[result_template_option.ResultTemplateOption] = None
    # Indicates the kind of contents to be searched when a search is performed using application permissions. Optional.
    share_point_one_drive_options: Optional[share_point_one_drive_options.SharePointOneDriveOptions] = None
    # The size of the page to be retrieved. The maximum value is 500. Optional.
    size: Optional[int] = None
    # Contains the ordered collection of fields and direction to sort results. There can be at most 5 sort properties in the collection. Optional.
    sort_properties: Optional[List[sort_property.SortProperty]] = None
    # The stored_fields property
    stored_fields: Optional[List[str]] = None
    # Indicates whether to trim away the duplicate SharePoint files from search results. Default value is false. Optional.
    trim_duplicates: Optional[bool] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import aggregation_option, collapse_property, entity_type, result_template_option, search_alteration_options, search_query, share_point_one_drive_options, sort_property

        fields: Dict[str, Callable[[Any], None]] = {
            "aggregations": lambda n : setattr(self, 'aggregations', n.get_collection_of_object_values(aggregation_option.AggregationOption)),
            "aggregationFilters": lambda n : setattr(self, 'aggregation_filters', n.get_collection_of_primitive_values(str)),
            "collapseProperties": lambda n : setattr(self, 'collapse_properties', n.get_collection_of_object_values(collapse_property.CollapseProperty)),
            "contentSources": lambda n : setattr(self, 'content_sources', n.get_collection_of_primitive_values(str)),
            "enableTopResults": lambda n : setattr(self, 'enable_top_results', n.get_bool_value()),
            "entityTypes": lambda n : setattr(self, 'entity_types', n.get_collection_of_enum_values(entity_type.EntityType)),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_primitive_values(str)),
            "from": lambda n : setattr(self, 'from_', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "query": lambda n : setattr(self, 'query', n.get_object_value(search_query.SearchQuery)),
            "queryAlterationOptions": lambda n : setattr(self, 'query_alteration_options', n.get_object_value(search_alteration_options.SearchAlterationOptions)),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "resultTemplateOptions": lambda n : setattr(self, 'result_template_options', n.get_object_value(result_template_option.ResultTemplateOption)),
            "sharePointOneDriveOptions": lambda n : setattr(self, 'share_point_one_drive_options', n.get_object_value(share_point_one_drive_options.SharePointOneDriveOptions)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "sortProperties": lambda n : setattr(self, 'sort_properties', n.get_collection_of_object_values(sort_property.SortProperty)),
            "stored_fields": lambda n : setattr(self, 'stored_fields', n.get_collection_of_primitive_values(str)),
            "trimDuplicates": lambda n : setattr(self, 'trim_duplicates', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("aggregations", self.aggregations)
        writer.write_collection_of_primitive_values("aggregationFilters", self.aggregation_filters)
        writer.write_collection_of_object_values("collapseProperties", self.collapse_properties)
        writer.write_collection_of_primitive_values("contentSources", self.content_sources)
        writer.write_bool_value("enableTopResults", self.enable_top_results)
        writer.write_enum_value("entityTypes", self.entity_types)
        writer.write_collection_of_primitive_values("fields", self.fields)
        writer.write_int_value("from", self.from_)
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
    

