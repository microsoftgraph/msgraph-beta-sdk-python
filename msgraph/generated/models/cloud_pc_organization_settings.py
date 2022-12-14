from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_operating_system = lazy_import('msgraph.generated.models.cloud_pc_operating_system')
cloud_pc_user_account_type = lazy_import('msgraph.generated.models.cloud_pc_user_account_type')
cloud_pc_windows_settings = lazy_import('msgraph.generated.models.cloud_pc_windows_settings')
entity = lazy_import('msgraph.generated.models.entity')

class CloudPcOrganizationSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcOrganizationSettings and sets the default values.
        """
        super().__init__()
        # Specifies whether new Cloud PCs will be automatically enrolled in Microsoft Endpoint Manager(MEM). The default value is false.
        self._enable_m_e_m_auto_enroll: Optional[bool] = None
        # The enableSingleSignOn property
        self._enable_single_sign_on: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The version of the operating system (OS) to provision on Cloud PCs. The possible values are: windows10, windows11, unknownFutureValue.
        self._os_version: Optional[cloud_pc_operating_system.CloudPcOperatingSystem] = None
        # The account type of the user on provisioned Cloud PCs. The possible values are: standardUser, administrator, unknownFutureValue.
        self._user_account_type: Optional[cloud_pc_user_account_type.CloudPcUserAccountType] = None
        # Represents the Cloud PC organization settings for a tenant. A tenant has only one cloudPcOrganizationSettings object. The default language value en-US.
        self._windows_settings: Optional[cloud_pc_windows_settings.CloudPcWindowsSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcOrganizationSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcOrganizationSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcOrganizationSettings()
    
    @property
    def enable_m_e_m_auto_enroll(self,) -> Optional[bool]:
        """
        Gets the enableMEMAutoEnroll property value. Specifies whether new Cloud PCs will be automatically enrolled in Microsoft Endpoint Manager(MEM). The default value is false.
        Returns: Optional[bool]
        """
        return self._enable_m_e_m_auto_enroll
    
    @enable_m_e_m_auto_enroll.setter
    def enable_m_e_m_auto_enroll(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableMEMAutoEnroll property value. Specifies whether new Cloud PCs will be automatically enrolled in Microsoft Endpoint Manager(MEM). The default value is false.
        Args:
            value: Value to set for the enableMEMAutoEnroll property.
        """
        self._enable_m_e_m_auto_enroll = value
    
    @property
    def enable_single_sign_on(self,) -> Optional[bool]:
        """
        Gets the enableSingleSignOn property value. The enableSingleSignOn property
        Returns: Optional[bool]
        """
        return self._enable_single_sign_on
    
    @enable_single_sign_on.setter
    def enable_single_sign_on(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableSingleSignOn property value. The enableSingleSignOn property
        Args:
            value: Value to set for the enableSingleSignOn property.
        """
        self._enable_single_sign_on = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enable_m_e_m_auto_enroll": lambda n : setattr(self, 'enable_m_e_m_auto_enroll', n.get_bool_value()),
            "enable_single_sign_on": lambda n : setattr(self, 'enable_single_sign_on', n.get_bool_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_enum_value(cloud_pc_operating_system.CloudPcOperatingSystem)),
            "user_account_type": lambda n : setattr(self, 'user_account_type', n.get_enum_value(cloud_pc_user_account_type.CloudPcUserAccountType)),
            "windows_settings": lambda n : setattr(self, 'windows_settings', n.get_object_value(cloud_pc_windows_settings.CloudPcWindowsSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def os_version(self,) -> Optional[cloud_pc_operating_system.CloudPcOperatingSystem]:
        """
        Gets the osVersion property value. The version of the operating system (OS) to provision on Cloud PCs. The possible values are: windows10, windows11, unknownFutureValue.
        Returns: Optional[cloud_pc_operating_system.CloudPcOperatingSystem]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[cloud_pc_operating_system.CloudPcOperatingSystem] = None) -> None:
        """
        Sets the osVersion property value. The version of the operating system (OS) to provision on Cloud PCs. The possible values are: windows10, windows11, unknownFutureValue.
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("enableMEMAutoEnroll", self.enable_m_e_m_auto_enroll)
        writer.write_bool_value("enableSingleSignOn", self.enable_single_sign_on)
        writer.write_enum_value("osVersion", self.os_version)
        writer.write_enum_value("userAccountType", self.user_account_type)
        writer.write_object_value("windowsSettings", self.windows_settings)
    
    @property
    def user_account_type(self,) -> Optional[cloud_pc_user_account_type.CloudPcUserAccountType]:
        """
        Gets the userAccountType property value. The account type of the user on provisioned Cloud PCs. The possible values are: standardUser, administrator, unknownFutureValue.
        Returns: Optional[cloud_pc_user_account_type.CloudPcUserAccountType]
        """
        return self._user_account_type
    
    @user_account_type.setter
    def user_account_type(self,value: Optional[cloud_pc_user_account_type.CloudPcUserAccountType] = None) -> None:
        """
        Sets the userAccountType property value. The account type of the user on provisioned Cloud PCs. The possible values are: standardUser, administrator, unknownFutureValue.
        Args:
            value: Value to set for the userAccountType property.
        """
        self._user_account_type = value
    
    @property
    def windows_settings(self,) -> Optional[cloud_pc_windows_settings.CloudPcWindowsSettings]:
        """
        Gets the windowsSettings property value. Represents the Cloud PC organization settings for a tenant. A tenant has only one cloudPcOrganizationSettings object. The default language value en-US.
        Returns: Optional[cloud_pc_windows_settings.CloudPcWindowsSettings]
        """
        return self._windows_settings
    
    @windows_settings.setter
    def windows_settings(self,value: Optional[cloud_pc_windows_settings.CloudPcWindowsSettings] = None) -> None:
        """
        Sets the windowsSettings property value. Represents the Cloud PC organization settings for a tenant. A tenant has only one cloudPcOrganizationSettings object. The default language value en-US.
        Args:
            value: Value to set for the windowsSettings property.
        """
        self._windows_settings = value
    

