from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

conditional_access_filter = lazy_import('msgraph.generated.models.conditional_access_filter')

class ConditionalAccessDevices(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessDevices and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Filter that defines the dynamic-device-syntax rule to include/exclude devices. A filter can use device properties (such as extension attributes) to include/exclude them. Cannot be set if includeDevices or excludeDevices is set.
        self._device_filter: Optional[conditional_access_filter.ConditionalAccessFilter] = None
        # States excluded from the scope of the policy. Possible values: Compliant, DomainJoined. Cannot be set if deviceFIlter is set.
        self._exclude_devices: Optional[List[str]] = None
        # The excludeDeviceStates property
        self._exclude_device_states: Optional[List[str]] = None
        # States in the scope of the policy. All is the only allowed value. Cannot be set if deviceFIlter is set.
        self._include_devices: Optional[List[str]] = None
        # The includeDeviceStates property
        self._include_device_states: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessDevices:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessDevices
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessDevices()
    
    @property
    def device_filter(self,) -> Optional[conditional_access_filter.ConditionalAccessFilter]:
        """
        Gets the deviceFilter property value. Filter that defines the dynamic-device-syntax rule to include/exclude devices. A filter can use device properties (such as extension attributes) to include/exclude them. Cannot be set if includeDevices or excludeDevices is set.
        Returns: Optional[conditional_access_filter.ConditionalAccessFilter]
        """
        return self._device_filter
    
    @device_filter.setter
    def device_filter(self,value: Optional[conditional_access_filter.ConditionalAccessFilter] = None) -> None:
        """
        Sets the deviceFilter property value. Filter that defines the dynamic-device-syntax rule to include/exclude devices. A filter can use device properties (such as extension attributes) to include/exclude them. Cannot be set if includeDevices or excludeDevices is set.
        Args:
            value: Value to set for the deviceFilter property.
        """
        self._device_filter = value
    
    @property
    def exclude_devices(self,) -> Optional[List[str]]:
        """
        Gets the excludeDevices property value. States excluded from the scope of the policy. Possible values: Compliant, DomainJoined. Cannot be set if deviceFIlter is set.
        Returns: Optional[List[str]]
        """
        return self._exclude_devices
    
    @exclude_devices.setter
    def exclude_devices(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludeDevices property value. States excluded from the scope of the policy. Possible values: Compliant, DomainJoined. Cannot be set if deviceFIlter is set.
        Args:
            value: Value to set for the excludeDevices property.
        """
        self._exclude_devices = value
    
    @property
    def exclude_device_states(self,) -> Optional[List[str]]:
        """
        Gets the excludeDeviceStates property value. The excludeDeviceStates property
        Returns: Optional[List[str]]
        """
        return self._exclude_device_states
    
    @exclude_device_states.setter
    def exclude_device_states(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludeDeviceStates property value. The excludeDeviceStates property
        Args:
            value: Value to set for the excludeDeviceStates property.
        """
        self._exclude_device_states = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_filter": lambda n : setattr(self, 'device_filter', n.get_object_value(conditional_access_filter.ConditionalAccessFilter)),
            "exclude_devices": lambda n : setattr(self, 'exclude_devices', n.get_collection_of_primitive_values(str)),
            "exclude_device_states": lambda n : setattr(self, 'exclude_device_states', n.get_collection_of_primitive_values(str)),
            "include_devices": lambda n : setattr(self, 'include_devices', n.get_collection_of_primitive_values(str)),
            "include_device_states": lambda n : setattr(self, 'include_device_states', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def include_devices(self,) -> Optional[List[str]]:
        """
        Gets the includeDevices property value. States in the scope of the policy. All is the only allowed value. Cannot be set if deviceFIlter is set.
        Returns: Optional[List[str]]
        """
        return self._include_devices
    
    @include_devices.setter
    def include_devices(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the includeDevices property value. States in the scope of the policy. All is the only allowed value. Cannot be set if deviceFIlter is set.
        Args:
            value: Value to set for the includeDevices property.
        """
        self._include_devices = value
    
    @property
    def include_device_states(self,) -> Optional[List[str]]:
        """
        Gets the includeDeviceStates property value. The includeDeviceStates property
        Returns: Optional[List[str]]
        """
        return self._include_device_states
    
    @include_device_states.setter
    def include_device_states(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the includeDeviceStates property value. The includeDeviceStates property
        Args:
            value: Value to set for the includeDeviceStates property.
        """
        self._include_device_states = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("deviceFilter", self.device_filter)
        writer.write_collection_of_primitive_values("excludeDevices", self.exclude_devices)
        writer.write_collection_of_primitive_values("excludeDeviceStates", self.exclude_device_states)
        writer.write_collection_of_primitive_values("includeDevices", self.include_devices)
        writer.write_collection_of_primitive_values("includeDeviceStates", self.include_device_states)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

