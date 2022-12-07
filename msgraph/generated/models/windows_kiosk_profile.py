from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_kiosk_app_configuration = lazy_import('msgraph.generated.models.windows_kiosk_app_configuration')
windows_kiosk_user = lazy_import('msgraph.generated.models.windows_kiosk_user')

class WindowsKioskProfile(AdditionalDataHolder, Parsable):
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
    def app_configuration(self,) -> Optional[windows_kiosk_app_configuration.WindowsKioskAppConfiguration]:
        """
        Gets the appConfiguration property value. The app base class used to identify the application info for the kiosk configuration
        Returns: Optional[windows_kiosk_app_configuration.WindowsKioskAppConfiguration]
        """
        return self._app_configuration
    
    @app_configuration.setter
    def app_configuration(self,value: Optional[windows_kiosk_app_configuration.WindowsKioskAppConfiguration] = None) -> None:
        """
        Sets the appConfiguration property value. The app base class used to identify the application info for the kiosk configuration
        Args:
            value: Value to set for the appConfiguration property.
        """
        self._app_configuration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsKioskProfile and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The app base class used to identify the application info for the kiosk configuration
        self._app_configuration: Optional[windows_kiosk_app_configuration.WindowsKioskAppConfiguration] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Key of the entity.
        self._profile_id: Optional[str] = None
        # This is a friendly name used to identify a group of applications, the layout of these apps on the start menu and the users to whom this kiosk configuration is assigned.
        self._profile_name: Optional[str] = None
        # The user accounts that will be locked to this kiosk configuration. This collection can contain a maximum of 100 elements.
        self._user_accounts_configuration: Optional[List[windows_kiosk_user.WindowsKioskUser]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsKioskProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_configuration": lambda n : setattr(self, 'app_configuration', n.get_object_value(windows_kiosk_app_configuration.WindowsKioskAppConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "profile_name": lambda n : setattr(self, 'profile_name', n.get_str_value()),
            "user_accounts_configuration": lambda n : setattr(self, 'user_accounts_configuration', n.get_collection_of_object_values(windows_kiosk_user.WindowsKioskUser)),
        }
        return fields
    
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
    
    @property
    def profile_id(self,) -> Optional[str]:
        """
        Gets the profileId property value. Key of the entity.
        Returns: Optional[str]
        """
        return self._profile_id
    
    @profile_id.setter
    def profile_id(self,value: Optional[str] = None) -> None:
        """
        Sets the profileId property value. Key of the entity.
        Args:
            value: Value to set for the profileId property.
        """
        self._profile_id = value
    
    @property
    def profile_name(self,) -> Optional[str]:
        """
        Gets the profileName property value. This is a friendly name used to identify a group of applications, the layout of these apps on the start menu and the users to whom this kiosk configuration is assigned.
        Returns: Optional[str]
        """
        return self._profile_name
    
    @profile_name.setter
    def profile_name(self,value: Optional[str] = None) -> None:
        """
        Sets the profileName property value. This is a friendly name used to identify a group of applications, the layout of these apps on the start menu and the users to whom this kiosk configuration is assigned.
        Args:
            value: Value to set for the profileName property.
        """
        self._profile_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("appConfiguration", self.app_configuration)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("profileId", self.profile_id)
        writer.write_str_value("profileName", self.profile_name)
        writer.write_collection_of_object_values("userAccountsConfiguration", self.user_accounts_configuration)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_accounts_configuration(self,) -> Optional[List[windows_kiosk_user.WindowsKioskUser]]:
        """
        Gets the userAccountsConfiguration property value. The user accounts that will be locked to this kiosk configuration. This collection can contain a maximum of 100 elements.
        Returns: Optional[List[windows_kiosk_user.WindowsKioskUser]]
        """
        return self._user_accounts_configuration
    
    @user_accounts_configuration.setter
    def user_accounts_configuration(self,value: Optional[List[windows_kiosk_user.WindowsKioskUser]] = None) -> None:
        """
        Sets the userAccountsConfiguration property value. The user accounts that will be locked to this kiosk configuration. This collection can contain a maximum of 100 elements.
        Args:
            value: Value to set for the userAccountsConfiguration property.
        """
        self._user_accounts_configuration = value
    

