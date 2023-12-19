from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .audit_log_query_record_type_filters import AuditLogQuery_recordTypeFilters
    from .audit_log_query_status import AuditLogQuery_status
    from .audit_log_record import AuditLogRecord

from ..entity import Entity

@dataclass
class AuditLogQuery(Entity):
    # The administrativeUnitIdFilters property
    administrative_unit_id_filters: Optional[List[str]] = None
    # The displayName property
    display_name: Optional[str] = None
    # The filterEndDateTime property
    filter_end_date_time: Optional[datetime.datetime] = None
    # The filterStartDateTime property
    filter_start_date_time: Optional[datetime.datetime] = None
    # The ipAddressFilters property
    ip_address_filters: Optional[List[str]] = None
    # The keywordFilter property
    keyword_filter: Optional[str] = None
    # The objectIdFilters property
    object_id_filters: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operationFilters property
    operation_filters: Optional[List[str]] = None
    # The recordTypeFilters property
    record_type_filters: Optional[List[AuditLogQuery_recordTypeFilters]] = None
    # The records property
    records: Optional[List[AuditLogRecord]] = None
    # The serviceFilters property
    service_filters: Optional[List[str]] = None
    # The status property
    status: Optional[AuditLogQuery_status] = None
    # The userPrincipalNameFilters property
    user_principal_name_filters: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuditLogQuery:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditLogQuery
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuditLogQuery()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .audit_log_query_record_type_filters import AuditLogQuery_recordTypeFilters
        from .audit_log_query_status import AuditLogQuery_status
        from .audit_log_record import AuditLogRecord

        from ..entity import Entity
        from .audit_log_query_record_type_filters import AuditLogQuery_recordTypeFilters
        from .audit_log_query_status import AuditLogQuery_status
        from .audit_log_record import AuditLogRecord

        fields: Dict[str, Callable[[Any], None]] = {
            "administrativeUnitIdFilters": lambda n : setattr(self, 'administrative_unit_id_filters', n.get_collection_of_primitive_values(str)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "filterEndDateTime": lambda n : setattr(self, 'filter_end_date_time', n.get_datetime_value()),
            "filterStartDateTime": lambda n : setattr(self, 'filter_start_date_time', n.get_datetime_value()),
            "ipAddressFilters": lambda n : setattr(self, 'ip_address_filters', n.get_collection_of_primitive_values(str)),
            "keywordFilter": lambda n : setattr(self, 'keyword_filter', n.get_str_value()),
            "objectIdFilters": lambda n : setattr(self, 'object_id_filters', n.get_collection_of_primitive_values(str)),
            "operationFilters": lambda n : setattr(self, 'operation_filters', n.get_collection_of_primitive_values(str)),
            "recordTypeFilters": lambda n : setattr(self, 'record_type_filters', n.get_collection_of_enum_values(AuditLogQuery_recordTypeFilters)),
            "records": lambda n : setattr(self, 'records', n.get_collection_of_object_values(AuditLogRecord)),
            "serviceFilters": lambda n : setattr(self, 'service_filters', n.get_collection_of_primitive_values(str)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AuditLogQuery_status)),
            "userPrincipalNameFilters": lambda n : setattr(self, 'user_principal_name_filters', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("administrativeUnitIdFilters", self.administrative_unit_id_filters)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("filterEndDateTime", self.filter_end_date_time)
        writer.write_datetime_value("filterStartDateTime", self.filter_start_date_time)
        writer.write_collection_of_primitive_values("ipAddressFilters", self.ip_address_filters)
        writer.write_str_value("keywordFilter", self.keyword_filter)
        writer.write_collection_of_primitive_values("objectIdFilters", self.object_id_filters)
        writer.write_collection_of_primitive_values("operationFilters", self.operation_filters)
        writer.write_collection_of_enum_values("recordTypeFilters", self.record_type_filters)
        writer.write_collection_of_object_values("records", self.records)
        writer.write_collection_of_primitive_values("serviceFilters", self.service_filters)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_primitive_values("userPrincipalNameFilters", self.user_principal_name_filters)
    

