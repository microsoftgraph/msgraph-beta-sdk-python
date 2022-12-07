from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
add_to_review_set_operation = lazy_import('msgraph.generated.models.ediscovery.add_to_review_set_operation')
data_source = lazy_import('msgraph.generated.models.ediscovery.data_source')
data_source_scopes = lazy_import('msgraph.generated.models.ediscovery.data_source_scopes')
estimate_statistics_operation = lazy_import('msgraph.generated.models.ediscovery.estimate_statistics_operation')
noncustodial_data_source = lazy_import('msgraph.generated.models.ediscovery.noncustodial_data_source')

class SourceCollection(entity.Entity):
    @property
    def additional_sources(self,) -> Optional[List[data_source.DataSource]]:
        """
        Gets the additionalSources property value. Adds an additional source to the sourceCollection.
        Returns: Optional[List[data_source.DataSource]]
        """
        return self._additional_sources
    
    @additional_sources.setter
    def additional_sources(self,value: Optional[List[data_source.DataSource]] = None) -> None:
        """
        Sets the additionalSources property value. Adds an additional source to the sourceCollection.
        Args:
            value: Value to set for the additionalSources property.
        """
        self._additional_sources = value
    
    @property
    def add_to_review_set_operation(self,) -> Optional[add_to_review_set_operation.AddToReviewSetOperation]:
        """
        Gets the addToReviewSetOperation property value. Adds the results of the sourceCollection to the specified reviewSet.
        Returns: Optional[add_to_review_set_operation.AddToReviewSetOperation]
        """
        return self._add_to_review_set_operation
    
    @add_to_review_set_operation.setter
    def add_to_review_set_operation(self,value: Optional[add_to_review_set_operation.AddToReviewSetOperation] = None) -> None:
        """
        Sets the addToReviewSetOperation property value. Adds the results of the sourceCollection to the specified reviewSet.
        Args:
            value: Value to set for the addToReviewSetOperation property.
        """
        self._add_to_review_set_operation = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new sourceCollection and sets the default values.
        """
        super().__init__()
        # Adds an additional source to the sourceCollection.
        self._additional_sources: Optional[List[data_source.DataSource]] = None
        # Adds the results of the sourceCollection to the specified reviewSet.
        self._add_to_review_set_operation: Optional[add_to_review_set_operation.AddToReviewSetOperation] = None
        # The query string in KQL (Keyword Query Language) query. For details, see Keyword queries and search conditions for Content Search and eDiscovery. You can refine searches by using fields paired with values; for example, subject:'Quarterly Financials' AND Date>=06/01/2016 AND Date<=07/01/2016.
        self._content_query: Optional[str] = None
        # The user who created the sourceCollection.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The date and time the sourceCollection was created.
        self._created_date_time: Optional[datetime] = None
        # Custodian sources that are included in the sourceCollection.
        self._custodian_sources: Optional[List[data_source.DataSource]] = None
        # When specified, the collection will span across a service for an entire workload. Possible values are: none, allTenantMailboxes, allTenantSites, allCaseCustodians, allCaseNoncustodialDataSources.
        self._data_source_scopes: Optional[data_source_scopes.DataSourceScopes] = None
        # The description of the sourceCollection.
        self._description: Optional[str] = None
        # The display name of the sourceCollection.
        self._display_name: Optional[str] = None
        # The last estimate operation associated with the sourceCollection.
        self._last_estimate_statistics_operation: Optional[estimate_statistics_operation.EstimateStatisticsOperation] = None
        # The last user who modified the sourceCollection.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The last date and time the sourceCollection was modified.
        self._last_modified_date_time: Optional[datetime] = None
        # noncustodialDataSource sources that are included in the sourceCollection
        self._noncustodial_sources: Optional[List[noncustodial_data_source.NoncustodialDataSource]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def content_query(self,) -> Optional[str]:
        """
        Gets the contentQuery property value. The query string in KQL (Keyword Query Language) query. For details, see Keyword queries and search conditions for Content Search and eDiscovery. You can refine searches by using fields paired with values; for example, subject:'Quarterly Financials' AND Date>=06/01/2016 AND Date<=07/01/2016.
        Returns: Optional[str]
        """
        return self._content_query
    
    @content_query.setter
    def content_query(self,value: Optional[str] = None) -> None:
        """
        Sets the contentQuery property value. The query string in KQL (Keyword Query Language) query. For details, see Keyword queries and search conditions for Content Search and eDiscovery. You can refine searches by using fields paired with values; for example, subject:'Quarterly Financials' AND Date>=06/01/2016 AND Date<=07/01/2016.
        Args:
            value: Value to set for the contentQuery property.
        """
        self._content_query = value
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The user who created the sourceCollection.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The user who created the sourceCollection.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the sourceCollection was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the sourceCollection was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SourceCollection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SourceCollection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SourceCollection()
    
    @property
    def custodian_sources(self,) -> Optional[List[data_source.DataSource]]:
        """
        Gets the custodianSources property value. Custodian sources that are included in the sourceCollection.
        Returns: Optional[List[data_source.DataSource]]
        """
        return self._custodian_sources
    
    @custodian_sources.setter
    def custodian_sources(self,value: Optional[List[data_source.DataSource]] = None) -> None:
        """
        Sets the custodianSources property value. Custodian sources that are included in the sourceCollection.
        Args:
            value: Value to set for the custodianSources property.
        """
        self._custodian_sources = value
    
    @property
    def data_source_scopes(self,) -> Optional[data_source_scopes.DataSourceScopes]:
        """
        Gets the dataSourceScopes property value. When specified, the collection will span across a service for an entire workload. Possible values are: none, allTenantMailboxes, allTenantSites, allCaseCustodians, allCaseNoncustodialDataSources.
        Returns: Optional[data_source_scopes.DataSourceScopes]
        """
        return self._data_source_scopes
    
    @data_source_scopes.setter
    def data_source_scopes(self,value: Optional[data_source_scopes.DataSourceScopes] = None) -> None:
        """
        Sets the dataSourceScopes property value. When specified, the collection will span across a service for an entire workload. Possible values are: none, allTenantMailboxes, allTenantSites, allCaseCustodians, allCaseNoncustodialDataSources.
        Args:
            value: Value to set for the dataSourceScopes property.
        """
        self._data_source_scopes = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the sourceCollection.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the sourceCollection.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the sourceCollection.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the sourceCollection.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "additional_sources": lambda n : setattr(self, 'additional_sources', n.get_collection_of_object_values(data_source.DataSource)),
            "add_to_review_set_operation": lambda n : setattr(self, 'add_to_review_set_operation', n.get_object_value(add_to_review_set_operation.AddToReviewSetOperation)),
            "content_query": lambda n : setattr(self, 'content_query', n.get_str_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "custodian_sources": lambda n : setattr(self, 'custodian_sources', n.get_collection_of_object_values(data_source.DataSource)),
            "data_source_scopes": lambda n : setattr(self, 'data_source_scopes', n.get_enum_value(data_source_scopes.DataSourceScopes)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_estimate_statistics_operation": lambda n : setattr(self, 'last_estimate_statistics_operation', n.get_object_value(estimate_statistics_operation.EstimateStatisticsOperation)),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "noncustodial_sources": lambda n : setattr(self, 'noncustodial_sources', n.get_collection_of_object_values(noncustodial_data_source.NoncustodialDataSource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_estimate_statistics_operation(self,) -> Optional[estimate_statistics_operation.EstimateStatisticsOperation]:
        """
        Gets the lastEstimateStatisticsOperation property value. The last estimate operation associated with the sourceCollection.
        Returns: Optional[estimate_statistics_operation.EstimateStatisticsOperation]
        """
        return self._last_estimate_statistics_operation
    
    @last_estimate_statistics_operation.setter
    def last_estimate_statistics_operation(self,value: Optional[estimate_statistics_operation.EstimateStatisticsOperation] = None) -> None:
        """
        Sets the lastEstimateStatisticsOperation property value. The last estimate operation associated with the sourceCollection.
        Args:
            value: Value to set for the lastEstimateStatisticsOperation property.
        """
        self._last_estimate_statistics_operation = value
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. The last user who modified the sourceCollection.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. The last user who modified the sourceCollection.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The last date and time the sourceCollection was modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The last date and time the sourceCollection was modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def noncustodial_sources(self,) -> Optional[List[noncustodial_data_source.NoncustodialDataSource]]:
        """
        Gets the noncustodialSources property value. noncustodialDataSource sources that are included in the sourceCollection
        Returns: Optional[List[noncustodial_data_source.NoncustodialDataSource]]
        """
        return self._noncustodial_sources
    
    @noncustodial_sources.setter
    def noncustodial_sources(self,value: Optional[List[noncustodial_data_source.NoncustodialDataSource]] = None) -> None:
        """
        Sets the noncustodialSources property value. noncustodialDataSource sources that are included in the sourceCollection
        Args:
            value: Value to set for the noncustodialSources property.
        """
        self._noncustodial_sources = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("additionalSources", self.additional_sources)
        writer.write_object_value("addToReviewSetOperation", self.add_to_review_set_operation)
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
    

