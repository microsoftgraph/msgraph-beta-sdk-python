from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
case_operation = lazy_import('msgraph.generated.models.ediscovery.case_operation')
case_settings = lazy_import('msgraph.generated.models.ediscovery.case_settings')
case_status = lazy_import('msgraph.generated.models.ediscovery.case_status')
custodian = lazy_import('msgraph.generated.models.ediscovery.custodian')
legal_hold = lazy_import('msgraph.generated.models.ediscovery.legal_hold')
noncustodial_data_source = lazy_import('msgraph.generated.models.ediscovery.noncustodial_data_source')
review_set = lazy_import('msgraph.generated.models.ediscovery.review_set')
source_collection = lazy_import('msgraph.generated.models.ediscovery.source_collection')
tag = lazy_import('msgraph.generated.models.ediscovery.tag')

class Case(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def closed_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the closedBy property value. The user who closed the case.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._closed_by
    
    @closed_by.setter
    def closed_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the closedBy property value. The user who closed the case.
        Args:
            value: Value to set for the closedBy property.
        """
        self._closed_by = value
    
    @property
    def closed_date_time(self,) -> Optional[datetime]:
        """
        Gets the closedDateTime property value. The date and time when the case was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._closed_date_time
    
    @closed_date_time.setter
    def closed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the closedDateTime property value. The date and time when the case was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the closedDateTime property.
        """
        self._closed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new case and sets the default values.
        """
        super().__init__()
        # The user who closed the case.
        self._closed_by: Optional[identity_set.IdentitySet] = None
        # The date and time when the case was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._closed_date_time: Optional[datetime] = None
        # The date and time when the entity was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._created_date_time: Optional[datetime] = None
        # Returns a list of case custodian objects for this case.  Nullable.
        self._custodians: Optional[List[custodian.Custodian]] = None
        # The case description.
        self._description: Optional[str] = None
        # The case name.
        self._display_name: Optional[str] = None
        # The external case number for customer reference.
        self._external_id: Optional[str] = None
        # The last user who modified the entity.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The latest date and time when the case was modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._last_modified_date_time: Optional[datetime] = None
        # Returns a list of case legalHold objects for this case.  Nullable.
        self._legal_holds: Optional[List[legal_hold.LegalHold]] = None
        # Returns a list of case noncustodialDataSource objects for this case.  Nullable.
        self._noncustodial_data_sources: Optional[List[noncustodial_data_source.NoncustodialDataSource]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Returns a list of case operation objects for this case. Nullable.
        self._operations: Optional[List[case_operation.CaseOperation]] = None
        # Returns a list of reviewSet objects in the case. Read-only. Nullable.
        self._review_sets: Optional[List[review_set.ReviewSet]] = None
        # The settings property
        self._settings: Optional[case_settings.CaseSettings] = None
        # Returns a list of sourceCollection objects associated with this case.
        self._source_collections: Optional[List[source_collection.SourceCollection]] = None
        # The case status. Possible values are unknown, active, pendingDelete, closing, closed, and closedWithError. For details, see the following table.
        self._status: Optional[case_status.CaseStatus] = None
        # Returns a list of tag objects associated to this case.
        self._tags: Optional[List[tag.Tag]] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the entity was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the entity was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Case:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Case
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Case()
    
    @property
    def custodians(self,) -> Optional[List[custodian.Custodian]]:
        """
        Gets the custodians property value. Returns a list of case custodian objects for this case.  Nullable.
        Returns: Optional[List[custodian.Custodian]]
        """
        return self._custodians
    
    @custodians.setter
    def custodians(self,value: Optional[List[custodian.Custodian]] = None) -> None:
        """
        Sets the custodians property value. Returns a list of case custodian objects for this case.  Nullable.
        Args:
            value: Value to set for the custodians property.
        """
        self._custodians = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The case description.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The case description.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The case name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The case name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. The external case number for customer reference.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. The external case number for customer reference.
        Args:
            value: Value to set for the externalId property.
        """
        self._external_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "closed_by": lambda n : setattr(self, 'closed_by', n.get_object_value(identity_set.IdentitySet)),
            "closed_date_time": lambda n : setattr(self, 'closed_date_time', n.get_datetime_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "custodians": lambda n : setattr(self, 'custodians', n.get_collection_of_object_values(custodian.Custodian)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "legal_holds": lambda n : setattr(self, 'legal_holds', n.get_collection_of_object_values(legal_hold.LegalHold)),
            "noncustodial_data_sources": lambda n : setattr(self, 'noncustodial_data_sources', n.get_collection_of_object_values(noncustodial_data_source.NoncustodialDataSource)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(case_operation.CaseOperation)),
            "review_sets": lambda n : setattr(self, 'review_sets', n.get_collection_of_object_values(review_set.ReviewSet)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(case_settings.CaseSettings)),
            "source_collections": lambda n : setattr(self, 'source_collections', n.get_collection_of_object_values(source_collection.SourceCollection)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(case_status.CaseStatus)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(tag.Tag)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. The last user who modified the entity.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. The last user who modified the entity.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The latest date and time when the case was modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The latest date and time when the case was modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def legal_holds(self,) -> Optional[List[legal_hold.LegalHold]]:
        """
        Gets the legalHolds property value. Returns a list of case legalHold objects for this case.  Nullable.
        Returns: Optional[List[legal_hold.LegalHold]]
        """
        return self._legal_holds
    
    @legal_holds.setter
    def legal_holds(self,value: Optional[List[legal_hold.LegalHold]] = None) -> None:
        """
        Sets the legalHolds property value. Returns a list of case legalHold objects for this case.  Nullable.
        Args:
            value: Value to set for the legalHolds property.
        """
        self._legal_holds = value
    
    @property
    def noncustodial_data_sources(self,) -> Optional[List[noncustodial_data_source.NoncustodialDataSource]]:
        """
        Gets the noncustodialDataSources property value. Returns a list of case noncustodialDataSource objects for this case.  Nullable.
        Returns: Optional[List[noncustodial_data_source.NoncustodialDataSource]]
        """
        return self._noncustodial_data_sources
    
    @noncustodial_data_sources.setter
    def noncustodial_data_sources(self,value: Optional[List[noncustodial_data_source.NoncustodialDataSource]] = None) -> None:
        """
        Sets the noncustodialDataSources property value. Returns a list of case noncustodialDataSource objects for this case.  Nullable.
        Args:
            value: Value to set for the noncustodialDataSources property.
        """
        self._noncustodial_data_sources = value
    
    @property
    def operations(self,) -> Optional[List[case_operation.CaseOperation]]:
        """
        Gets the operations property value. Returns a list of case operation objects for this case. Nullable.
        Returns: Optional[List[case_operation.CaseOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[case_operation.CaseOperation]] = None) -> None:
        """
        Sets the operations property value. Returns a list of case operation objects for this case. Nullable.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def review_sets(self,) -> Optional[List[review_set.ReviewSet]]:
        """
        Gets the reviewSets property value. Returns a list of reviewSet objects in the case. Read-only. Nullable.
        Returns: Optional[List[review_set.ReviewSet]]
        """
        return self._review_sets
    
    @review_sets.setter
    def review_sets(self,value: Optional[List[review_set.ReviewSet]] = None) -> None:
        """
        Sets the reviewSets property value. Returns a list of reviewSet objects in the case. Read-only. Nullable.
        Args:
            value: Value to set for the reviewSets property.
        """
        self._review_sets = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("closedBy", self.closed_by)
        writer.write_datetime_value("closedDateTime", self.closed_date_time)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("custodians", self.custodians)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("legalHolds", self.legal_holds)
        writer.write_collection_of_object_values("noncustodialDataSources", self.noncustodial_data_sources)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("reviewSets", self.review_sets)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("sourceCollections", self.source_collections)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_object_values("tags", self.tags)
    
    @property
    def settings(self,) -> Optional[case_settings.CaseSettings]:
        """
        Gets the settings property value. The settings property
        Returns: Optional[case_settings.CaseSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[case_settings.CaseSettings] = None) -> None:
        """
        Sets the settings property value. The settings property
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def source_collections(self,) -> Optional[List[source_collection.SourceCollection]]:
        """
        Gets the sourceCollections property value. Returns a list of sourceCollection objects associated with this case.
        Returns: Optional[List[source_collection.SourceCollection]]
        """
        return self._source_collections
    
    @source_collections.setter
    def source_collections(self,value: Optional[List[source_collection.SourceCollection]] = None) -> None:
        """
        Sets the sourceCollections property value. Returns a list of sourceCollection objects associated with this case.
        Args:
            value: Value to set for the sourceCollections property.
        """
        self._source_collections = value
    
    @property
    def status(self,) -> Optional[case_status.CaseStatus]:
        """
        Gets the status property value. The case status. Possible values are unknown, active, pendingDelete, closing, closed, and closedWithError. For details, see the following table.
        Returns: Optional[case_status.CaseStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[case_status.CaseStatus] = None) -> None:
        """
        Sets the status property value. The case status. Possible values are unknown, active, pendingDelete, closing, closed, and closedWithError. For details, see the following table.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def tags(self,) -> Optional[List[tag.Tag]]:
        """
        Gets the tags property value. Returns a list of tag objects associated to this case.
        Returns: Optional[List[tag.Tag]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[tag.Tag]] = None) -> None:
        """
        Sets the tags property value. Returns a list of tag objects associated to this case.
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    

