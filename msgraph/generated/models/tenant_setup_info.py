from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
privileged_role_settings = lazy_import('msgraph.generated.models.privileged_role_settings')
setup_status = lazy_import('msgraph.generated.models.setup_status')

class TenantSetupInfo(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new TenantSetupInfo and sets the default values.
        """
        super().__init__()
        # The defaultRolesSettings property
        self._default_roles_settings: Optional[privileged_role_settings.PrivilegedRoleSettings] = None
        # The firstTimeSetup property
        self._first_time_setup: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The relevantRolesSettings property
        self._relevant_roles_settings: Optional[List[str]] = None
        # The setupStatus property
        self._setup_status: Optional[setup_status.SetupStatus] = None
        # The skipSetup property
        self._skip_setup: Optional[bool] = None
        # The userRolesActions property
        self._user_roles_actions: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantSetupInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantSetupInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TenantSetupInfo()
    
    @property
    def default_roles_settings(self,) -> Optional[privileged_role_settings.PrivilegedRoleSettings]:
        """
        Gets the defaultRolesSettings property value. The defaultRolesSettings property
        Returns: Optional[privileged_role_settings.PrivilegedRoleSettings]
        """
        return self._default_roles_settings
    
    @default_roles_settings.setter
    def default_roles_settings(self,value: Optional[privileged_role_settings.PrivilegedRoleSettings] = None) -> None:
        """
        Sets the defaultRolesSettings property value. The defaultRolesSettings property
        Args:
            value: Value to set for the defaultRolesSettings property.
        """
        self._default_roles_settings = value
    
    @property
    def first_time_setup(self,) -> Optional[bool]:
        """
        Gets the firstTimeSetup property value. The firstTimeSetup property
        Returns: Optional[bool]
        """
        return self._first_time_setup
    
    @first_time_setup.setter
    def first_time_setup(self,value: Optional[bool] = None) -> None:
        """
        Sets the firstTimeSetup property value. The firstTimeSetup property
        Args:
            value: Value to set for the firstTimeSetup property.
        """
        self._first_time_setup = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_roles_settings": lambda n : setattr(self, 'default_roles_settings', n.get_object_value(privileged_role_settings.PrivilegedRoleSettings)),
            "first_time_setup": lambda n : setattr(self, 'first_time_setup', n.get_bool_value()),
            "relevant_roles_settings": lambda n : setattr(self, 'relevant_roles_settings', n.get_collection_of_primitive_values(str)),
            "setup_status": lambda n : setattr(self, 'setup_status', n.get_enum_value(setup_status.SetupStatus)),
            "skip_setup": lambda n : setattr(self, 'skip_setup', n.get_bool_value()),
            "user_roles_actions": lambda n : setattr(self, 'user_roles_actions', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def relevant_roles_settings(self,) -> Optional[List[str]]:
        """
        Gets the relevantRolesSettings property value. The relevantRolesSettings property
        Returns: Optional[List[str]]
        """
        return self._relevant_roles_settings
    
    @relevant_roles_settings.setter
    def relevant_roles_settings(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the relevantRolesSettings property value. The relevantRolesSettings property
        Args:
            value: Value to set for the relevantRolesSettings property.
        """
        self._relevant_roles_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("defaultRolesSettings", self.default_roles_settings)
        writer.write_bool_value("firstTimeSetup", self.first_time_setup)
        writer.write_collection_of_primitive_values("relevantRolesSettings", self.relevant_roles_settings)
        writer.write_enum_value("setupStatus", self.setup_status)
        writer.write_bool_value("skipSetup", self.skip_setup)
        writer.write_str_value("userRolesActions", self.user_roles_actions)
    
    @property
    def setup_status(self,) -> Optional[setup_status.SetupStatus]:
        """
        Gets the setupStatus property value. The setupStatus property
        Returns: Optional[setup_status.SetupStatus]
        """
        return self._setup_status
    
    @setup_status.setter
    def setup_status(self,value: Optional[setup_status.SetupStatus] = None) -> None:
        """
        Sets the setupStatus property value. The setupStatus property
        Args:
            value: Value to set for the setupStatus property.
        """
        self._setup_status = value
    
    @property
    def skip_setup(self,) -> Optional[bool]:
        """
        Gets the skipSetup property value. The skipSetup property
        Returns: Optional[bool]
        """
        return self._skip_setup
    
    @skip_setup.setter
    def skip_setup(self,value: Optional[bool] = None) -> None:
        """
        Sets the skipSetup property value. The skipSetup property
        Args:
            value: Value to set for the skipSetup property.
        """
        self._skip_setup = value
    
    @property
    def user_roles_actions(self,) -> Optional[str]:
        """
        Gets the userRolesActions property value. The userRolesActions property
        Returns: Optional[str]
        """
        return self._user_roles_actions
    
    @user_roles_actions.setter
    def user_roles_actions(self,value: Optional[str] = None) -> None:
        """
        Sets the userRolesActions property value. The userRolesActions property
        Args:
            value: Value to set for the userRolesActions property.
        """
        self._user_roles_actions = value
    

