from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .audit_data import AuditData
    from .audit_log_record_audit_log_record_type import AuditLogRecord_auditLogRecordType
    from .audit_log_record_user_type import AuditLogRecord_userType

from ..entity import Entity

@dataclass
class AuditLogRecord(Entity):
    # The administrativeUnits property
    administrative_units: Optional[List[str]] = None
    # The auditData property
    audit_data: Optional[AuditData] = None
    # The auditLogRecordType property
    audit_log_record_type: Optional[AuditLogRecord_auditLogRecordType] = None
    # The clientIp property
    client_ip: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The objectId property
    object_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operation property
    operation: Optional[str] = None
    # The organizationId property
    organization_id: Optional[str] = None
    # The service property
    service: Optional[str] = None
    # The userId property
    user_id: Optional[str] = None
    # The userPrincipalName property
    user_principal_name: Optional[str] = None
    # The userType property
    user_type: Optional[AuditLogRecord_userType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuditLogRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditLogRecord
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuditLogRecord()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .audit_data import AuditData
        from .audit_log_record_audit_log_record_type import AuditLogRecord_auditLogRecordType
        from .audit_log_record_user_type import AuditLogRecord_userType

        from ..entity import Entity
        from .audit_data import AuditData
        from .audit_log_record_audit_log_record_type import AuditLogRecord_auditLogRecordType
        from .audit_log_record_user_type import AuditLogRecord_userType

        fields: Dict[str, Callable[[Any], None]] = {
            "administrativeUnits": lambda n : setattr(self, 'administrative_units', n.get_collection_of_primitive_values(str)),
            "auditData": lambda n : setattr(self, 'audit_data', n.get_object_value(AuditData)),
            "auditLogRecordType": lambda n : setattr(self, 'audit_log_record_type', n.get_enum_value(AuditLogRecord_auditLogRecordType)),
            "clientIp": lambda n : setattr(self, 'client_ip', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "objectId": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "operation": lambda n : setattr(self, 'operation', n.get_str_value()),
            "organizationId": lambda n : setattr(self, 'organization_id', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(AuditLogRecord_userType)),
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
        writer.write_collection_of_primitive_values("administrativeUnits", self.administrative_units)
        writer.write_object_value("auditData", self.audit_data)
        writer.write_enum_value("auditLogRecordType", self.audit_log_record_type)
        writer.write_str_value("clientIp", self.client_ip)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("objectId", self.object_id)
        writer.write_str_value("operation", self.operation)
        writer.write_str_value("organizationId", self.organization_id)
        writer.write_str_value("service", self.service)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_enum_value("userType", self.user_type)
    

