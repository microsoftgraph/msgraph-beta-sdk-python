from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import add_to_review_set_operation, data_source, data_source_scopes, estimate_statistics_operation, noncustodial_data_source
    from .. import entity, identity_set

from .. import entity

@dataclass
class SourceCollection(entity.Entity):
    # Adds the results of the sourceCollection to the specified reviewSet.
    add_to_review_set_operation: Optional[add_to_review_set_operation.AddToReviewSetOperation] = None
    # Adds an additional source to the sourceCollection.
    additional_sources: Optional[List[data_source.DataSource]] = None
    # The query string in KQL (Keyword Query Language) query. For details, see Keyword queries and search conditions for Content Search and eDiscovery. You can refine searches by using fields paired with values; for example, subject:'Quarterly Financials' AND Date>=06/01/2016 AND Date<=07/01/2016.
    content_query: Optional[str] = None
    # The user who created the sourceCollection.
    created_by: Optional[identity_set.IdentitySet] = None
    # The date and time the sourceCollection was created.
    created_date_time: Optional[datetime] = None
    # Custodian sources that are included in the sourceCollection.
    custodian_sources: Optional[List[data_source.DataSource]] = None
    # When specified, the collection will span across a service for an entire workload. Possible values are: none, allTenantMailboxes, allTenantSites, allCaseCustodians, allCaseNoncustodialDataSources.
    data_source_scopes: Optional[data_source_scopes.DataSourceScopes] = None
    # The description of the sourceCollection.
    description: Optional[str] = None
    # The display name of the sourceCollection.
    display_name: Optional[str] = None
    # The last estimate operation associated with the sourceCollection.
    last_estimate_statistics_operation: Optional[estimate_statistics_operation.EstimateStatisticsOperation] = None
    # The last user who modified the sourceCollection.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # The last date and time the sourceCollection was modified.
    last_modified_date_time: Optional[datetime] = None
    # noncustodialDataSource sources that are included in the sourceCollection
    noncustodial_sources: Optional[List[noncustodial_data_source.NoncustodialDataSource]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SourceCollection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SourceCollection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SourceCollection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import add_to_review_set_operation, data_source, data_source_scopes, estimate_statistics_operation, noncustodial_data_source
        from .. import entity, identity_set

        from . import add_to_review_set_operation, data_source, data_source_scopes, estimate_statistics_operation, noncustodial_data_source
        from .. import entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "addToReviewSetOperation": lambda n : setattr(self, 'add_to_review_set_operation', n.get_object_value(add_to_review_set_operation.AddToReviewSetOperation)),
            "additionalSources": lambda n : setattr(self, 'additional_sources', n.get_collection_of_object_values(data_source.DataSource)),
            "contentQuery": lambda n : setattr(self, 'content_query', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "custodianSources": lambda n : setattr(self, 'custodian_sources', n.get_collection_of_object_values(data_source.DataSource)),
            "dataSourceScopes": lambda n : setattr(self, 'data_source_scopes', n.get_enum_value(data_source_scopes.DataSourceScopes)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastEstimateStatisticsOperation": lambda n : setattr(self, 'last_estimate_statistics_operation', n.get_object_value(estimate_statistics_operation.EstimateStatisticsOperation)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "noncustodialSources": lambda n : setattr(self, 'noncustodial_sources', n.get_collection_of_object_values(noncustodial_data_source.NoncustodialDataSource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("addToReviewSetOperation", self.add_to_review_set_operation)
        writer.write_collection_of_object_values("additionalSources", self.additional_sources)
        writer.write_str_value("contentQuery", self.content_query)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("custodianSources", self.custodian_sources)
        writer.write_enum_value("dataSourceScopes", self.data_source_scopes)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("lastEstimateStatisticsOperation", self.last_estimate_statistics_operation)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("noncustodialSources", self.noncustodial_sources)
    

