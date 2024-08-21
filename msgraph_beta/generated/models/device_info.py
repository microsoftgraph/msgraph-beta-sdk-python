from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The deviceId property
    device_id: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The enrollmentProfileName property
    enrollment_profile_name: Optional[str] = None
    # The extensionAttribute1 property
    extension_attribute1: Optional[str] = None
    # The extensionAttribute10 property
    extension_attribute10: Optional[str] = None
    # The extensionAttribute11 property
    extension_attribute11: Optional[str] = None
    # The extensionAttribute12 property
    extension_attribute12: Optional[str] = None
    # The extensionAttribute13 property
    extension_attribute13: Optional[str] = None
    # The extensionAttribute14 property
    extension_attribute14: Optional[str] = None
    # The extensionAttribute15 property
    extension_attribute15: Optional[str] = None
    # The extensionAttribute2 property
    extension_attribute2: Optional[str] = None
    # The extensionAttribute3 property
    extension_attribute3: Optional[str] = None
    # The extensionAttribute4 property
    extension_attribute4: Optional[str] = None
    # The extensionAttribute5 property
    extension_attribute5: Optional[str] = None
    # The extensionAttribute6 property
    extension_attribute6: Optional[str] = None
    # The extensionAttribute7 property
    extension_attribute7: Optional[str] = None
    # The extensionAttribute8 property
    extension_attribute8: Optional[str] = None
    # The extensionAttribute9 property
    extension_attribute9: Optional[str] = None
    # The isCompliant property
    is_compliant: Optional[bool] = None
    # The manufacturer property
    manufacturer: Optional[str] = None
    # The mdmAppId property
    mdm_app_id: Optional[str] = None
    # The model property
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operatingSystem property
    operating_system: Optional[str] = None
    # The operatingSystemVersion property
    operating_system_version: Optional[str] = None
    # The ownership property
    ownership: Optional[str] = None
    # The physicalIds property
    physical_ids: Optional[List[str]] = None
    # The profileType property
    profile_type: Optional[str] = None
    # The systemLabels property
    system_labels: Optional[List[str]] = None
    # The trustType property
    trust_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrollmentProfileName": lambda n : setattr(self, 'enrollment_profile_name', n.get_str_value()),
            "extensionAttribute1": lambda n : setattr(self, 'extension_attribute1', n.get_str_value()),
            "extensionAttribute10": lambda n : setattr(self, 'extension_attribute10', n.get_str_value()),
            "extensionAttribute11": lambda n : setattr(self, 'extension_attribute11', n.get_str_value()),
            "extensionAttribute12": lambda n : setattr(self, 'extension_attribute12', n.get_str_value()),
            "extensionAttribute13": lambda n : setattr(self, 'extension_attribute13', n.get_str_value()),
            "extensionAttribute14": lambda n : setattr(self, 'extension_attribute14', n.get_str_value()),
            "extensionAttribute15": lambda n : setattr(self, 'extension_attribute15', n.get_str_value()),
            "extensionAttribute2": lambda n : setattr(self, 'extension_attribute2', n.get_str_value()),
            "extensionAttribute3": lambda n : setattr(self, 'extension_attribute3', n.get_str_value()),
            "extensionAttribute4": lambda n : setattr(self, 'extension_attribute4', n.get_str_value()),
            "extensionAttribute5": lambda n : setattr(self, 'extension_attribute5', n.get_str_value()),
            "extensionAttribute6": lambda n : setattr(self, 'extension_attribute6', n.get_str_value()),
            "extensionAttribute7": lambda n : setattr(self, 'extension_attribute7', n.get_str_value()),
            "extensionAttribute8": lambda n : setattr(self, 'extension_attribute8', n.get_str_value()),
            "extensionAttribute9": lambda n : setattr(self, 'extension_attribute9', n.get_str_value()),
            "isCompliant": lambda n : setattr(self, 'is_compliant', n.get_bool_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "mdmAppId": lambda n : setattr(self, 'mdm_app_id', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "operatingSystemVersion": lambda n : setattr(self, 'operating_system_version', n.get_str_value()),
            "ownership": lambda n : setattr(self, 'ownership', n.get_str_value()),
            "physicalIds": lambda n : setattr(self, 'physical_ids', n.get_collection_of_primitive_values(str)),
            "profileType": lambda n : setattr(self, 'profile_type', n.get_str_value()),
            "systemLabels": lambda n : setattr(self, 'system_labels', n.get_collection_of_primitive_values(str)),
            "trustType": lambda n : setattr(self, 'trust_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("enrollmentProfileName", self.enrollment_profile_name)
        writer.write_str_value("extensionAttribute1", self.extension_attribute1)
        writer.write_str_value("extensionAttribute10", self.extension_attribute10)
        writer.write_str_value("extensionAttribute11", self.extension_attribute11)
        writer.write_str_value("extensionAttribute12", self.extension_attribute12)
        writer.write_str_value("extensionAttribute13", self.extension_attribute13)
        writer.write_str_value("extensionAttribute14", self.extension_attribute14)
        writer.write_str_value("extensionAttribute15", self.extension_attribute15)
        writer.write_str_value("extensionAttribute2", self.extension_attribute2)
        writer.write_str_value("extensionAttribute3", self.extension_attribute3)
        writer.write_str_value("extensionAttribute4", self.extension_attribute4)
        writer.write_str_value("extensionAttribute5", self.extension_attribute5)
        writer.write_str_value("extensionAttribute6", self.extension_attribute6)
        writer.write_str_value("extensionAttribute7", self.extension_attribute7)
        writer.write_str_value("extensionAttribute8", self.extension_attribute8)
        writer.write_str_value("extensionAttribute9", self.extension_attribute9)
        writer.write_bool_value("isCompliant", self.is_compliant)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("mdmAppId", self.mdm_app_id)
        writer.write_str_value("model", self.model)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_str_value("operatingSystemVersion", self.operating_system_version)
        writer.write_str_value("ownership", self.ownership)
        writer.write_collection_of_primitive_values("physicalIds", self.physical_ids)
        writer.write_str_value("profileType", self.profile_type)
        writer.write_collection_of_primitive_values("systemLabels", self.system_labels)
        writer.write_str_value("trustType", self.trust_type)
        writer.write_additional_data_value(self.additional_data)
    

