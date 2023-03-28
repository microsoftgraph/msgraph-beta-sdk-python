from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class DeviceDetail(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new deviceDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates the browser information of the used for signing-in.
        self._browser: Optional[str] = None
        # The browserId property
        self._browser_id: Optional[str] = None
        # Refers to the UniqueID of the device used for signing-in.
        self._device_id: Optional[str] = None
        # Refers to the name of the device used for signing-in.
        self._display_name: Optional[str] = None
        # Indicates whether the device is compliant or not.
        self._is_compliant: Optional[bool] = None
        # Indicates if the device is managed or not.
        self._is_managed: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates the OS name and version used for signing-in.
        self._operating_system: Optional[str] = None
        # Indicates information on whether the signed-in device is Workplace Joined, AzureAD Joined, Domain Joined.
        self._trust_type: Optional[str] = None
    
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
    
    @property
    def browser(self,) -> Optional[str]:
        """
        Gets the browser property value. Indicates the browser information of the used for signing-in.
        Returns: Optional[str]
        """
        return self._browser
    
    @browser.setter
    def browser(self,value: Optional[str] = None) -> None:
        """
        Sets the browser property value. Indicates the browser information of the used for signing-in.
        Args:
            value: Value to set for the browser property.
        """
        self._browser = value
    
    @property
    def browser_id(self,) -> Optional[str]:
        """
        Gets the browserId property value. The browserId property
        Returns: Optional[str]
        """
        return self._browser_id
    
    @browser_id.setter
    def browser_id(self,value: Optional[str] = None) -> None:
        """
        Sets the browserId property value. The browserId property
        Args:
            value: Value to set for the browser_id property.
        """
        self._browser_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceDetail()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. Refers to the UniqueID of the device used for signing-in.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. Refers to the UniqueID of the device used for signing-in.
        Args:
            value: Value to set for the device_id property.
        """
        self._device_id = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Refers to the name of the device used for signing-in.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Refers to the name of the device used for signing-in.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "browserId": lambda n : setattr(self, 'browser_id', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isCompliant": lambda n : setattr(self, 'is_compliant', n.get_bool_value()),
            "isManaged": lambda n : setattr(self, 'is_managed', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "trustType": lambda n : setattr(self, 'trust_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_compliant(self,) -> Optional[bool]:
        """
        Gets the isCompliant property value. Indicates whether the device is compliant or not.
        Returns: Optional[bool]
        """
        return self._is_compliant
    
    @is_compliant.setter
    def is_compliant(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCompliant property value. Indicates whether the device is compliant or not.
        Args:
            value: Value to set for the is_compliant property.
        """
        self._is_compliant = value
    
    @property
    def is_managed(self,) -> Optional[bool]:
        """
        Gets the isManaged property value. Indicates if the device is managed or not.
        Returns: Optional[bool]
        """
        return self._is_managed
    
    @is_managed.setter
    def is_managed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isManaged property value. Indicates if the device is managed or not.
        Args:
            value: Value to set for the is_managed property.
        """
        self._is_managed = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def operating_system(self,) -> Optional[str]:
        """
        Gets the operatingSystem property value. Indicates the OS name and version used for signing-in.
        Returns: Optional[str]
        """
        return self._operating_system
    
    @operating_system.setter
    def operating_system(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystem property value. Indicates the OS name and version used for signing-in.
        Args:
            value: Value to set for the operating_system property.
        """
        self._operating_system = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("browser", self.browser)
        writer.write_str_value("browserId", self.browser_id)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isCompliant", self.is_compliant)
        writer.write_bool_value("isManaged", self.is_managed)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_str_value("trustType", self.trust_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def trust_type(self,) -> Optional[str]:
        """
        Gets the trustType property value. Indicates information on whether the signed-in device is Workplace Joined, AzureAD Joined, Domain Joined.
        Returns: Optional[str]
        """
        return self._trust_type
    
    @trust_type.setter
    def trust_type(self,value: Optional[str] = None) -> None:
        """
        Sets the trustType property value. Indicates information on whether the signed-in device is Workplace Joined, AzureAD Joined, Domain Joined.
        Args:
            value: Value to set for the trust_type property.
        """
        self._trust_type = value
    

