from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app_intent = lazy_import('msgraph.generated.models.mobile_app_intent')
mobile_app_supported_device_type = lazy_import('msgraph.generated.models.mobile_app_supported_device_type')
resultant_app_state = lazy_import('msgraph.generated.models.resultant_app_state')

class MobileAppIntentAndStateDetail(AdditionalDataHolder, Parsable):
    """
    Mobile App Intent and Install State for a given device.
    """
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
    def application_id(self,) -> Optional[str]:
        """
        Gets the applicationId property value. MobieApp identifier.
        Returns: Optional[str]
        """
        return self._application_id
    
    @application_id.setter
    def application_id(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationId property value. MobieApp identifier.
        Args:
            value: Value to set for the applicationId property.
        """
        self._application_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new mobileAppIntentAndStateDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # MobieApp identifier.
        self._application_id: Optional[str] = None
        # The admin provided or imported title of the app.
        self._display_name: Optional[str] = None
        # Human readable version of the application
        self._display_version: Optional[str] = None
        # A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
        self._install_state: Optional[resultant_app_state.ResultantAppState] = None
        # Indicates the status of the mobile app on the device.
        self._mobile_app_intent: Optional[mobile_app_intent.MobileAppIntent] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The supported platforms for the app.
        self._supported_device_types: Optional[List[mobile_app_supported_device_type.MobileAppSupportedDeviceType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppIntentAndStateDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppIntentAndStateDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppIntentAndStateDetail()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The admin provided or imported title of the app.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The admin provided or imported title of the app.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def display_version(self,) -> Optional[str]:
        """
        Gets the displayVersion property value. Human readable version of the application
        Returns: Optional[str]
        """
        return self._display_version
    
    @display_version.setter
    def display_version(self,value: Optional[str] = None) -> None:
        """
        Sets the displayVersion property value. Human readable version of the application
        Args:
            value: Value to set for the displayVersion property.
        """
        self._display_version = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_id": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "display_version": lambda n : setattr(self, 'display_version', n.get_str_value()),
            "install_state": lambda n : setattr(self, 'install_state', n.get_enum_value(resultant_app_state.ResultantAppState)),
            "mobile_app_intent": lambda n : setattr(self, 'mobile_app_intent', n.get_enum_value(mobile_app_intent.MobileAppIntent)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "supported_device_types": lambda n : setattr(self, 'supported_device_types', n.get_collection_of_object_values(mobile_app_supported_device_type.MobileAppSupportedDeviceType)),
        }
        return fields
    
    @property
    def install_state(self,) -> Optional[resultant_app_state.ResultantAppState]:
        """
        Gets the installState property value. A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
        Returns: Optional[resultant_app_state.ResultantAppState]
        """
        return self._install_state
    
    @install_state.setter
    def install_state(self,value: Optional[resultant_app_state.ResultantAppState] = None) -> None:
        """
        Sets the installState property value. A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
        Args:
            value: Value to set for the installState property.
        """
        self._install_state = value
    
    @property
    def mobile_app_intent(self,) -> Optional[mobile_app_intent.MobileAppIntent]:
        """
        Gets the mobileAppIntent property value. Indicates the status of the mobile app on the device.
        Returns: Optional[mobile_app_intent.MobileAppIntent]
        """
        return self._mobile_app_intent
    
    @mobile_app_intent.setter
    def mobile_app_intent(self,value: Optional[mobile_app_intent.MobileAppIntent] = None) -> None:
        """
        Sets the mobileAppIntent property value. Indicates the status of the mobile app on the device.
        Args:
            value: Value to set for the mobileAppIntent property.
        """
        self._mobile_app_intent = value
    
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
        writer.write_str_value("applicationId", self.application_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("displayVersion", self.display_version)
        writer.write_enum_value("installState", self.install_state)
        writer.write_enum_value("mobileAppIntent", self.mobile_app_intent)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("supportedDeviceTypes", self.supported_device_types)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def supported_device_types(self,) -> Optional[List[mobile_app_supported_device_type.MobileAppSupportedDeviceType]]:
        """
        Gets the supportedDeviceTypes property value. The supported platforms for the app.
        Returns: Optional[List[mobile_app_supported_device_type.MobileAppSupportedDeviceType]]
        """
        return self._supported_device_types
    
    @supported_device_types.setter
    def supported_device_types(self,value: Optional[List[mobile_app_supported_device_type.MobileAppSupportedDeviceType]] = None) -> None:
        """
        Sets the supportedDeviceTypes property value. The supported platforms for the app.
        Args:
            value: Value to set for the supportedDeviceTypes property.
        """
        self._supported_device_types = value
    

