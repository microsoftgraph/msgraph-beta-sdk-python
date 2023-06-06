from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import enrollment_state, entity, imported_device_identity_result, imported_device_identity_type, platform

from . import entity

@dataclass
class ImportedDeviceIdentity(entity.Entity):
    """
    The importedDeviceIdentity resource represents a unique hardware identity of a device that has been pre-staged for pre-enrollment configuration.
    """
    # Created Date Time of the device
    created_date_time: Optional[datetime] = None
    # The description of the device
    description: Optional[str] = None
    # The enrollmentState property
    enrollment_state: Optional[enrollment_state.EnrollmentState] = None
    # Imported Device Identifier
    imported_device_identifier: Optional[str] = None
    # The importedDeviceIdentityType property
    imported_device_identity_type: Optional[imported_device_identity_type.ImportedDeviceIdentityType] = None
    # Last Contacted Date Time of the device
    last_contacted_date_time: Optional[datetime] = None
    # Last Modified DateTime of the description
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The platform property
    platform: Optional[platform.Platform] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImportedDeviceIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ImportedDeviceIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.importedDeviceIdentityResult":
                from . import imported_device_identity_result

                return imported_device_identity_result.ImportedDeviceIdentityResult()
        return ImportedDeviceIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import enrollment_state, entity, imported_device_identity_result, imported_device_identity_type, platform

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "enrollmentState": lambda n : setattr(self, 'enrollment_state', n.get_enum_value(enrollment_state.EnrollmentState)),
            "importedDeviceIdentifier": lambda n : setattr(self, 'imported_device_identifier', n.get_str_value()),
            "importedDeviceIdentityType": lambda n : setattr(self, 'imported_device_identity_type', n.get_enum_value(imported_device_identity_type.ImportedDeviceIdentityType)),
            "lastContactedDateTime": lambda n : setattr(self, 'last_contacted_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(platform.Platform)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("enrollmentState", self.enrollment_state)
        writer.write_str_value("importedDeviceIdentifier", self.imported_device_identifier)
        writer.write_enum_value("importedDeviceIdentityType", self.imported_device_identity_type)
        writer.write_datetime_value("lastContactedDateTime", self.last_contacted_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("platform", self.platform)
    

