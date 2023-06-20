from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import case_operation, case_settings, case_status, custodian, legal_hold, noncustodial_data_source, review_set, source_collection, tag
    from .. import entity, identity_set

from .. import entity

@dataclass
class Case(entity.Entity):
    # The user who closed the case.
    closed_by: Optional[identity_set.IdentitySet] = None
    # The date and time when the case was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    closed_date_time: Optional[datetime] = None
    # The date and time when the entity was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime] = None
    # Returns a list of case custodian objects for this case.  Nullable.
    custodians: Optional[List[custodian.Custodian]] = None
    # The case description.
    description: Optional[str] = None
    # The case name.
    display_name: Optional[str] = None
    # The external case number for customer reference.
    external_id: Optional[str] = None
    # The last user who modified the entity.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # The latest date and time when the case was modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_modified_date_time: Optional[datetime] = None
    # Returns a list of case legalHold objects for this case.  Nullable.
    legal_holds: Optional[List[legal_hold.LegalHold]] = None
    # Returns a list of case noncustodialDataSource objects for this case.  Nullable.
    noncustodial_data_sources: Optional[List[noncustodial_data_source.NoncustodialDataSource]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Returns a list of case operation objects for this case. Nullable.
    operations: Optional[List[case_operation.CaseOperation]] = None
    # Returns a list of reviewSet objects in the case. Read-only. Nullable.
    review_sets: Optional[List[review_set.ReviewSet]] = None
    # The settings property
    settings: Optional[case_settings.CaseSettings] = None
    # Returns a list of sourceCollection objects associated with this case.
    source_collections: Optional[List[source_collection.SourceCollection]] = None
    # The case status. Possible values are unknown, active, pendingDelete, closing, closed, and closedWithError. For details, see the following table.
    status: Optional[case_status.CaseStatus] = None
    # Returns a list of tag objects associated to this case.
    tags: Optional[List[tag.Tag]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Case:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Case
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Case()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import case_operation, case_settings, case_status, custodian, legal_hold, noncustodial_data_source, review_set, source_collection, tag
        from .. import entity, identity_set

        from . import case_operation, case_settings, case_status, custodian, legal_hold, noncustodial_data_source, review_set, source_collection, tag
        from .. import entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "closedBy": lambda n : setattr(self, 'closed_by', n.get_object_value(identity_set.IdentitySet)),
            "closedDateTime": lambda n : setattr(self, 'closed_date_time', n.get_datetime_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "custodians": lambda n : setattr(self, 'custodians', n.get_collection_of_object_values(custodian.Custodian)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "legalHolds": lambda n : setattr(self, 'legal_holds', n.get_collection_of_object_values(legal_hold.LegalHold)),
            "noncustodialDataSources": lambda n : setattr(self, 'noncustodial_data_sources', n.get_collection_of_object_values(noncustodial_data_source.NoncustodialDataSource)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(case_operation.CaseOperation)),
            "reviewSets": lambda n : setattr(self, 'review_sets', n.get_collection_of_object_values(review_set.ReviewSet)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(case_settings.CaseSettings)),
            "sourceCollections": lambda n : setattr(self, 'source_collections', n.get_collection_of_object_values(source_collection.SourceCollection)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(case_status.CaseStatus)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(tag.Tag)),
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
    

