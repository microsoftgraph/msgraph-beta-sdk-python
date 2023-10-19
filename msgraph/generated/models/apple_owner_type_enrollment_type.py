from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_user_initiated_enrollment_type import AppleUserInitiatedEnrollmentType
    from .managed_device_owner_type import ManagedDeviceOwnerType

@dataclass
class AppleOwnerTypeEnrollmentType(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The enrollmentType property
    enrollment_type: Optional[AppleUserInitiatedEnrollmentType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Owner type of device.
    owner_type: Optional[ManagedDeviceOwnerType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleOwnerTypeEnrollmentType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppleOwnerTypeEnrollmentType
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AppleOwnerTypeEnrollmentType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .apple_user_initiated_enrollment_type import AppleUserInitiatedEnrollmentType
        from .managed_device_owner_type import ManagedDeviceOwnerType

        from .apple_user_initiated_enrollment_type import AppleUserInitiatedEnrollmentType
        from .managed_device_owner_type import ManagedDeviceOwnerType

        fields: Dict[str, Callable[[Any], None]] = {
            "enrollmentType": lambda n : setattr(self, 'enrollment_type', n.get_enum_value(AppleUserInitiatedEnrollmentType)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ownerType": lambda n : setattr(self, 'owner_type', n.get_enum_value(ManagedDeviceOwnerType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("enrollmentType", self.enrollment_type)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("ownerType", self.owner_type)
        writer.write_additional_data_value(self.additional_data)
    

