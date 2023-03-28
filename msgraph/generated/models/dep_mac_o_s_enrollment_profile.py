from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import dep_enrollment_base_profile

from . import dep_enrollment_base_profile

class DepMacOSEnrollmentProfile(dep_enrollment_base_profile.DepEnrollmentBaseProfile):
    def __init__(self,) -> None:
        """
        Instantiates a new DepMacOSEnrollmentProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.depMacOSEnrollmentProfile"
        # Indicates if Accessibility screen is disabled
        self._accessibility_screen_disabled: Optional[bool] = None
        # Indicates what the full name for the admin account is
        self._admin_account_full_name: Optional[str] = None
        # Indicates what the password for the admin account is
        self._admin_account_password: Optional[str] = None
        # Indicates what the user name for the admin account is
        self._admin_account_user_name: Optional[str] = None
        # Indicates if UnlockWithWatch screen is disabled
        self._auto_unlock_with_watch_disabled: Optional[bool] = None
        # Indicates if iCloud Documents and Desktop screen is disabled
        self._choose_your_lock_screen_disabled: Optional[bool] = None
        # Indicates whether Setup Assistant will auto populate the primary account information
        self._dont_auto_populate_primary_account_info: Optional[bool] = None
        # Indicates whether the user will enable blockediting
        self._enable_restrict_editing: Optional[bool] = None
        # Indicates if file vault is disabled
        self._file_vault_disabled: Optional[bool] = None
        # Indicates whether the admin account should be hidded or not
        self._hide_admin_account: Optional[bool] = None
        # Indicates if iCloud Analytics screen is disabled
        self._i_cloud_diagnostics_disabled: Optional[bool] = None
        # Indicates if iCloud Documents and Desktop screen is disabled
        self._i_cloud_storage_disabled: Optional[bool] = None
        # Indicates if Passcode setup pane is disabled
        self._pass_code_disabled: Optional[bool] = None
        # Indicates what the full name for the primary account is
        self._primary_account_full_name: Optional[str] = None
        # Indicates what the account name for the primary account is
        self._primary_account_user_name: Optional[str] = None
        # Indicates if registration is disabled
        self._registration_disabled: Optional[bool] = None
        # Indicates if the device is network-tethered to run the command
        self._request_requires_network_tether: Optional[bool] = None
        # Indicates whether Setup Assistant will set the account as a regular user
        self._set_primary_setup_account_as_regular_user: Optional[bool] = None
        # Indicates whether Setup Assistant will skip the user interface for primary account setup
        self._skip_primary_setup_account_creation: Optional[bool] = None
        # Indicates if zoom setup pane is disabled
        self._zoom_disabled: Optional[bool] = None
    
    @property
    def accessibility_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the accessibilityScreenDisabled property value. Indicates if Accessibility screen is disabled
        Returns: Optional[bool]
        """
        return self._accessibility_screen_disabled
    
    @accessibility_screen_disabled.setter
    def accessibility_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the accessibilityScreenDisabled property value. Indicates if Accessibility screen is disabled
        Args:
            value: Value to set for the accessibility_screen_disabled property.
        """
        self._accessibility_screen_disabled = value
    
    @property
    def admin_account_full_name(self,) -> Optional[str]:
        """
        Gets the adminAccountFullName property value. Indicates what the full name for the admin account is
        Returns: Optional[str]
        """
        return self._admin_account_full_name
    
    @admin_account_full_name.setter
    def admin_account_full_name(self,value: Optional[str] = None) -> None:
        """
        Sets the adminAccountFullName property value. Indicates what the full name for the admin account is
        Args:
            value: Value to set for the admin_account_full_name property.
        """
        self._admin_account_full_name = value
    
    @property
    def admin_account_password(self,) -> Optional[str]:
        """
        Gets the adminAccountPassword property value. Indicates what the password for the admin account is
        Returns: Optional[str]
        """
        return self._admin_account_password
    
    @admin_account_password.setter
    def admin_account_password(self,value: Optional[str] = None) -> None:
        """
        Sets the adminAccountPassword property value. Indicates what the password for the admin account is
        Args:
            value: Value to set for the admin_account_password property.
        """
        self._admin_account_password = value
    
    @property
    def admin_account_user_name(self,) -> Optional[str]:
        """
        Gets the adminAccountUserName property value. Indicates what the user name for the admin account is
        Returns: Optional[str]
        """
        return self._admin_account_user_name
    
    @admin_account_user_name.setter
    def admin_account_user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the adminAccountUserName property value. Indicates what the user name for the admin account is
        Args:
            value: Value to set for the admin_account_user_name property.
        """
        self._admin_account_user_name = value
    
    @property
    def auto_unlock_with_watch_disabled(self,) -> Optional[bool]:
        """
        Gets the autoUnlockWithWatchDisabled property value. Indicates if UnlockWithWatch screen is disabled
        Returns: Optional[bool]
        """
        return self._auto_unlock_with_watch_disabled
    
    @auto_unlock_with_watch_disabled.setter
    def auto_unlock_with_watch_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the autoUnlockWithWatchDisabled property value. Indicates if UnlockWithWatch screen is disabled
        Args:
            value: Value to set for the auto_unlock_with_watch_disabled property.
        """
        self._auto_unlock_with_watch_disabled = value
    
    @property
    def choose_your_lock_screen_disabled(self,) -> Optional[bool]:
        """
        Gets the chooseYourLockScreenDisabled property value. Indicates if iCloud Documents and Desktop screen is disabled
        Returns: Optional[bool]
        """
        return self._choose_your_lock_screen_disabled
    
    @choose_your_lock_screen_disabled.setter
    def choose_your_lock_screen_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the chooseYourLockScreenDisabled property value. Indicates if iCloud Documents and Desktop screen is disabled
        Args:
            value: Value to set for the choose_your_lock_screen_disabled property.
        """
        self._choose_your_lock_screen_disabled = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DepMacOSEnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DepMacOSEnrollmentProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DepMacOSEnrollmentProfile()
    
    @property
    def dont_auto_populate_primary_account_info(self,) -> Optional[bool]:
        """
        Gets the dontAutoPopulatePrimaryAccountInfo property value. Indicates whether Setup Assistant will auto populate the primary account information
        Returns: Optional[bool]
        """
        return self._dont_auto_populate_primary_account_info
    
    @dont_auto_populate_primary_account_info.setter
    def dont_auto_populate_primary_account_info(self,value: Optional[bool] = None) -> None:
        """
        Sets the dontAutoPopulatePrimaryAccountInfo property value. Indicates whether Setup Assistant will auto populate the primary account information
        Args:
            value: Value to set for the dont_auto_populate_primary_account_info property.
        """
        self._dont_auto_populate_primary_account_info = value
    
    @property
    def enable_restrict_editing(self,) -> Optional[bool]:
        """
        Gets the enableRestrictEditing property value. Indicates whether the user will enable blockediting
        Returns: Optional[bool]
        """
        return self._enable_restrict_editing
    
    @enable_restrict_editing.setter
    def enable_restrict_editing(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableRestrictEditing property value. Indicates whether the user will enable blockediting
        Args:
            value: Value to set for the enable_restrict_editing property.
        """
        self._enable_restrict_editing = value
    
    @property
    def file_vault_disabled(self,) -> Optional[bool]:
        """
        Gets the fileVaultDisabled property value. Indicates if file vault is disabled
        Returns: Optional[bool]
        """
        return self._file_vault_disabled
    
    @file_vault_disabled.setter
    def file_vault_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the fileVaultDisabled property value. Indicates if file vault is disabled
        Args:
            value: Value to set for the file_vault_disabled property.
        """
        self._file_vault_disabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import dep_enrollment_base_profile

        fields: Dict[str, Callable[[Any], None]] = {
            "accessibilityScreenDisabled": lambda n : setattr(self, 'accessibility_screen_disabled', n.get_bool_value()),
            "adminAccountFullName": lambda n : setattr(self, 'admin_account_full_name', n.get_str_value()),
            "adminAccountPassword": lambda n : setattr(self, 'admin_account_password', n.get_str_value()),
            "adminAccountUserName": lambda n : setattr(self, 'admin_account_user_name', n.get_str_value()),
            "autoUnlockWithWatchDisabled": lambda n : setattr(self, 'auto_unlock_with_watch_disabled', n.get_bool_value()),
            "chooseYourLockScreenDisabled": lambda n : setattr(self, 'choose_your_lock_screen_disabled', n.get_bool_value()),
            "dontAutoPopulatePrimaryAccountInfo": lambda n : setattr(self, 'dont_auto_populate_primary_account_info', n.get_bool_value()),
            "enableRestrictEditing": lambda n : setattr(self, 'enable_restrict_editing', n.get_bool_value()),
            "fileVaultDisabled": lambda n : setattr(self, 'file_vault_disabled', n.get_bool_value()),
            "hideAdminAccount": lambda n : setattr(self, 'hide_admin_account', n.get_bool_value()),
            "iCloudDiagnosticsDisabled": lambda n : setattr(self, 'i_cloud_diagnostics_disabled', n.get_bool_value()),
            "iCloudStorageDisabled": lambda n : setattr(self, 'i_cloud_storage_disabled', n.get_bool_value()),
            "passCodeDisabled": lambda n : setattr(self, 'pass_code_disabled', n.get_bool_value()),
            "primaryAccountFullName": lambda n : setattr(self, 'primary_account_full_name', n.get_str_value()),
            "primaryAccountUserName": lambda n : setattr(self, 'primary_account_user_name', n.get_str_value()),
            "registrationDisabled": lambda n : setattr(self, 'registration_disabled', n.get_bool_value()),
            "requestRequiresNetworkTether": lambda n : setattr(self, 'request_requires_network_tether', n.get_bool_value()),
            "setPrimarySetupAccountAsRegularUser": lambda n : setattr(self, 'set_primary_setup_account_as_regular_user', n.get_bool_value()),
            "skipPrimarySetupAccountCreation": lambda n : setattr(self, 'skip_primary_setup_account_creation', n.get_bool_value()),
            "zoomDisabled": lambda n : setattr(self, 'zoom_disabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hide_admin_account(self,) -> Optional[bool]:
        """
        Gets the hideAdminAccount property value. Indicates whether the admin account should be hidded or not
        Returns: Optional[bool]
        """
        return self._hide_admin_account
    
    @hide_admin_account.setter
    def hide_admin_account(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideAdminAccount property value. Indicates whether the admin account should be hidded or not
        Args:
            value: Value to set for the hide_admin_account property.
        """
        self._hide_admin_account = value
    
    @property
    def i_cloud_diagnostics_disabled(self,) -> Optional[bool]:
        """
        Gets the iCloudDiagnosticsDisabled property value. Indicates if iCloud Analytics screen is disabled
        Returns: Optional[bool]
        """
        return self._i_cloud_diagnostics_disabled
    
    @i_cloud_diagnostics_disabled.setter
    def i_cloud_diagnostics_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudDiagnosticsDisabled property value. Indicates if iCloud Analytics screen is disabled
        Args:
            value: Value to set for the i_cloud_diagnostics_disabled property.
        """
        self._i_cloud_diagnostics_disabled = value
    
    @property
    def i_cloud_storage_disabled(self,) -> Optional[bool]:
        """
        Gets the iCloudStorageDisabled property value. Indicates if iCloud Documents and Desktop screen is disabled
        Returns: Optional[bool]
        """
        return self._i_cloud_storage_disabled
    
    @i_cloud_storage_disabled.setter
    def i_cloud_storage_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudStorageDisabled property value. Indicates if iCloud Documents and Desktop screen is disabled
        Args:
            value: Value to set for the i_cloud_storage_disabled property.
        """
        self._i_cloud_storage_disabled = value
    
    @property
    def pass_code_disabled(self,) -> Optional[bool]:
        """
        Gets the passCodeDisabled property value. Indicates if Passcode setup pane is disabled
        Returns: Optional[bool]
        """
        return self._pass_code_disabled
    
    @pass_code_disabled.setter
    def pass_code_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the passCodeDisabled property value. Indicates if Passcode setup pane is disabled
        Args:
            value: Value to set for the pass_code_disabled property.
        """
        self._pass_code_disabled = value
    
    @property
    def primary_account_full_name(self,) -> Optional[str]:
        """
        Gets the primaryAccountFullName property value. Indicates what the full name for the primary account is
        Returns: Optional[str]
        """
        return self._primary_account_full_name
    
    @primary_account_full_name.setter
    def primary_account_full_name(self,value: Optional[str] = None) -> None:
        """
        Sets the primaryAccountFullName property value. Indicates what the full name for the primary account is
        Args:
            value: Value to set for the primary_account_full_name property.
        """
        self._primary_account_full_name = value
    
    @property
    def primary_account_user_name(self,) -> Optional[str]:
        """
        Gets the primaryAccountUserName property value. Indicates what the account name for the primary account is
        Returns: Optional[str]
        """
        return self._primary_account_user_name
    
    @primary_account_user_name.setter
    def primary_account_user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the primaryAccountUserName property value. Indicates what the account name for the primary account is
        Args:
            value: Value to set for the primary_account_user_name property.
        """
        self._primary_account_user_name = value
    
    @property
    def registration_disabled(self,) -> Optional[bool]:
        """
        Gets the registrationDisabled property value. Indicates if registration is disabled
        Returns: Optional[bool]
        """
        return self._registration_disabled
    
    @registration_disabled.setter
    def registration_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the registrationDisabled property value. Indicates if registration is disabled
        Args:
            value: Value to set for the registration_disabled property.
        """
        self._registration_disabled = value
    
    @property
    def request_requires_network_tether(self,) -> Optional[bool]:
        """
        Gets the requestRequiresNetworkTether property value. Indicates if the device is network-tethered to run the command
        Returns: Optional[bool]
        """
        return self._request_requires_network_tether
    
    @request_requires_network_tether.setter
    def request_requires_network_tether(self,value: Optional[bool] = None) -> None:
        """
        Sets the requestRequiresNetworkTether property value. Indicates if the device is network-tethered to run the command
        Args:
            value: Value to set for the request_requires_network_tether property.
        """
        self._request_requires_network_tether = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("accessibilityScreenDisabled", self.accessibility_screen_disabled)
        writer.write_str_value("adminAccountFullName", self.admin_account_full_name)
        writer.write_str_value("adminAccountPassword", self.admin_account_password)
        writer.write_str_value("adminAccountUserName", self.admin_account_user_name)
        writer.write_bool_value("autoUnlockWithWatchDisabled", self.auto_unlock_with_watch_disabled)
        writer.write_bool_value("chooseYourLockScreenDisabled", self.choose_your_lock_screen_disabled)
        writer.write_bool_value("dontAutoPopulatePrimaryAccountInfo", self.dont_auto_populate_primary_account_info)
        writer.write_bool_value("enableRestrictEditing", self.enable_restrict_editing)
        writer.write_bool_value("fileVaultDisabled", self.file_vault_disabled)
        writer.write_bool_value("hideAdminAccount", self.hide_admin_account)
        writer.write_bool_value("iCloudDiagnosticsDisabled", self.i_cloud_diagnostics_disabled)
        writer.write_bool_value("iCloudStorageDisabled", self.i_cloud_storage_disabled)
        writer.write_bool_value("passCodeDisabled", self.pass_code_disabled)
        writer.write_str_value("primaryAccountFullName", self.primary_account_full_name)
        writer.write_str_value("primaryAccountUserName", self.primary_account_user_name)
        writer.write_bool_value("registrationDisabled", self.registration_disabled)
        writer.write_bool_value("requestRequiresNetworkTether", self.request_requires_network_tether)
        writer.write_bool_value("setPrimarySetupAccountAsRegularUser", self.set_primary_setup_account_as_regular_user)
        writer.write_bool_value("skipPrimarySetupAccountCreation", self.skip_primary_setup_account_creation)
        writer.write_bool_value("zoomDisabled", self.zoom_disabled)
    
    @property
    def set_primary_setup_account_as_regular_user(self,) -> Optional[bool]:
        """
        Gets the setPrimarySetupAccountAsRegularUser property value. Indicates whether Setup Assistant will set the account as a regular user
        Returns: Optional[bool]
        """
        return self._set_primary_setup_account_as_regular_user
    
    @set_primary_setup_account_as_regular_user.setter
    def set_primary_setup_account_as_regular_user(self,value: Optional[bool] = None) -> None:
        """
        Sets the setPrimarySetupAccountAsRegularUser property value. Indicates whether Setup Assistant will set the account as a regular user
        Args:
            value: Value to set for the set_primary_setup_account_as_regular_user property.
        """
        self._set_primary_setup_account_as_regular_user = value
    
    @property
    def skip_primary_setup_account_creation(self,) -> Optional[bool]:
        """
        Gets the skipPrimarySetupAccountCreation property value. Indicates whether Setup Assistant will skip the user interface for primary account setup
        Returns: Optional[bool]
        """
        return self._skip_primary_setup_account_creation
    
    @skip_primary_setup_account_creation.setter
    def skip_primary_setup_account_creation(self,value: Optional[bool] = None) -> None:
        """
        Sets the skipPrimarySetupAccountCreation property value. Indicates whether Setup Assistant will skip the user interface for primary account setup
        Args:
            value: Value to set for the skip_primary_setup_account_creation property.
        """
        self._skip_primary_setup_account_creation = value
    
    @property
    def zoom_disabled(self,) -> Optional[bool]:
        """
        Gets the zoomDisabled property value. Indicates if zoom setup pane is disabled
        Returns: Optional[bool]
        """
        return self._zoom_disabled
    
    @zoom_disabled.setter
    def zoom_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the zoomDisabled property value. Indicates if zoom setup pane is disabled
        Args:
            value: Value to set for the zoom_disabled property.
        """
        self._zoom_disabled = value
    

