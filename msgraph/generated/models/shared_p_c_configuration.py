from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
enablement = lazy_import('msgraph.generated.models.enablement')
shared_p_c_account_manager_policy = lazy_import('msgraph.generated.models.shared_p_c_account_manager_policy')
shared_p_c_allowed_account_type = lazy_import('msgraph.generated.models.shared_p_c_allowed_account_type')

class SharedPCConfiguration(device_configuration.DeviceConfiguration):
    @property
    def account_manager_policy(self,) -> Optional[shared_p_c_account_manager_policy.SharedPCAccountManagerPolicy]:
        """
        Gets the accountManagerPolicy property value. Specifies how accounts are managed on a shared PC. Only applies when disableAccountManager is false.
        Returns: Optional[shared_p_c_account_manager_policy.SharedPCAccountManagerPolicy]
        """
        return self._account_manager_policy
    
    @account_manager_policy.setter
    def account_manager_policy(self,value: Optional[shared_p_c_account_manager_policy.SharedPCAccountManagerPolicy] = None) -> None:
        """
        Sets the accountManagerPolicy property value. Specifies how accounts are managed on a shared PC. Only applies when disableAccountManager is false.
        Args:
            value: Value to set for the account_manager_policy property.
        """
        self._account_manager_policy = value
    
    @property
    def allow_local_storage(self,) -> Optional[bool]:
        """
        Gets the allowLocalStorage property value. Specifies whether local storage is allowed on a shared PC.
        Returns: Optional[bool]
        """
        return self._allow_local_storage
    
    @allow_local_storage.setter
    def allow_local_storage(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowLocalStorage property value. Specifies whether local storage is allowed on a shared PC.
        Args:
            value: Value to set for the allow_local_storage property.
        """
        self._allow_local_storage = value
    
    @property
    def allowed_accounts(self,) -> Optional[shared_p_c_allowed_account_type.SharedPCAllowedAccountType]:
        """
        Gets the allowedAccounts property value. Type of accounts that are allowed to share the PC.
        Returns: Optional[shared_p_c_allowed_account_type.SharedPCAllowedAccountType]
        """
        return self._allowed_accounts
    
    @allowed_accounts.setter
    def allowed_accounts(self,value: Optional[shared_p_c_allowed_account_type.SharedPCAllowedAccountType] = None) -> None:
        """
        Sets the allowedAccounts property value. Type of accounts that are allowed to share the PC.
        Args:
            value: Value to set for the allowed_accounts property.
        """
        self._allowed_accounts = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new SharedPCConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.sharedPCConfiguration"
        # Specifies how accounts are managed on a shared PC. Only applies when disableAccountManager is false.
        self._account_manager_policy: Optional[shared_p_c_account_manager_policy.SharedPCAccountManagerPolicy] = None
        # Specifies whether local storage is allowed on a shared PC.
        self._allow_local_storage: Optional[bool] = None
        # Type of accounts that are allowed to share the PC.
        self._allowed_accounts: Optional[shared_p_c_allowed_account_type.SharedPCAllowedAccountType] = None
        # Disables the account manager for shared PC mode.
        self._disable_account_manager: Optional[bool] = None
        # Specifies whether the default shared PC education environment policies should be disabled. For Windows 10 RS2 and later, this policy will be applied without setting Enabled to true.
        self._disable_edu_policies: Optional[bool] = None
        # Specifies whether the default shared PC power policies should be disabled.
        self._disable_power_policies: Optional[bool] = None
        # Disables the requirement to sign in whenever the device wakes up from sleep mode.
        self._disable_sign_in_on_resume: Optional[bool] = None
        # Enables shared PC mode and applies the shared pc policies.
        self._enabled: Optional[bool] = None
        # Possible values of a property
        self._fast_first_sign_in: Optional[enablement.Enablement] = None
        # Specifies the time in seconds that a device must sit idle before the PC goes to sleep. Setting this value to 0 prevents the sleep timeout from occurring.
        self._idle_time_before_sleep_in_seconds: Optional[int] = None
        # Specifies the display text for the account shown on the sign-in screen which launches the app specified by SetKioskAppUserModelId. Only applies when KioskAppUserModelId is set.
        self._kiosk_app_display_name: Optional[str] = None
        # Specifies the application user model ID of the app to use with assigned access.
        self._kiosk_app_user_model_id: Optional[str] = None
        # Possible values of a property
        self._local_storage: Optional[enablement.Enablement] = None
        # Specifies the daily start time of maintenance hour.
        self._maintenance_start_time: Optional[Time] = None
        # Possible values of a property
        self._set_account_manager: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._set_edu_policies: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._set_power_policies: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._sign_in_on_resume: Optional[enablement.Enablement] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharedPCConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharedPCConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharedPCConfiguration()
    
    @property
    def disable_account_manager(self,) -> Optional[bool]:
        """
        Gets the disableAccountManager property value. Disables the account manager for shared PC mode.
        Returns: Optional[bool]
        """
        return self._disable_account_manager
    
    @disable_account_manager.setter
    def disable_account_manager(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableAccountManager property value. Disables the account manager for shared PC mode.
        Args:
            value: Value to set for the disable_account_manager property.
        """
        self._disable_account_manager = value
    
    @property
    def disable_edu_policies(self,) -> Optional[bool]:
        """
        Gets the disableEduPolicies property value. Specifies whether the default shared PC education environment policies should be disabled. For Windows 10 RS2 and later, this policy will be applied without setting Enabled to true.
        Returns: Optional[bool]
        """
        return self._disable_edu_policies
    
    @disable_edu_policies.setter
    def disable_edu_policies(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableEduPolicies property value. Specifies whether the default shared PC education environment policies should be disabled. For Windows 10 RS2 and later, this policy will be applied without setting Enabled to true.
        Args:
            value: Value to set for the disable_edu_policies property.
        """
        self._disable_edu_policies = value
    
    @property
    def disable_power_policies(self,) -> Optional[bool]:
        """
        Gets the disablePowerPolicies property value. Specifies whether the default shared PC power policies should be disabled.
        Returns: Optional[bool]
        """
        return self._disable_power_policies
    
    @disable_power_policies.setter
    def disable_power_policies(self,value: Optional[bool] = None) -> None:
        """
        Sets the disablePowerPolicies property value. Specifies whether the default shared PC power policies should be disabled.
        Args:
            value: Value to set for the disable_power_policies property.
        """
        self._disable_power_policies = value
    
    @property
    def disable_sign_in_on_resume(self,) -> Optional[bool]:
        """
        Gets the disableSignInOnResume property value. Disables the requirement to sign in whenever the device wakes up from sleep mode.
        Returns: Optional[bool]
        """
        return self._disable_sign_in_on_resume
    
    @disable_sign_in_on_resume.setter
    def disable_sign_in_on_resume(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableSignInOnResume property value. Disables the requirement to sign in whenever the device wakes up from sleep mode.
        Args:
            value: Value to set for the disable_sign_in_on_resume property.
        """
        self._disable_sign_in_on_resume = value
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. Enables shared PC mode and applies the shared pc policies.
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. Enables shared PC mode and applies the shared pc policies.
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    @property
    def fast_first_sign_in(self,) -> Optional[enablement.Enablement]:
        """
        Gets the fastFirstSignIn property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._fast_first_sign_in
    
    @fast_first_sign_in.setter
    def fast_first_sign_in(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the fastFirstSignIn property value. Possible values of a property
        Args:
            value: Value to set for the fast_first_sign_in property.
        """
        self._fast_first_sign_in = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "accountManagerPolicy": lambda n : setattr(self, 'account_manager_policy', n.get_object_value(shared_p_c_account_manager_policy.SharedPCAccountManagerPolicy)),
            "allowedAccounts": lambda n : setattr(self, 'allowed_accounts', n.get_enum_value(shared_p_c_allowed_account_type.SharedPCAllowedAccountType)),
            "allowLocalStorage": lambda n : setattr(self, 'allow_local_storage', n.get_bool_value()),
            "disableAccountManager": lambda n : setattr(self, 'disable_account_manager', n.get_bool_value()),
            "disableEduPolicies": lambda n : setattr(self, 'disable_edu_policies', n.get_bool_value()),
            "disablePowerPolicies": lambda n : setattr(self, 'disable_power_policies', n.get_bool_value()),
            "disableSignInOnResume": lambda n : setattr(self, 'disable_sign_in_on_resume', n.get_bool_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "fastFirstSignIn": lambda n : setattr(self, 'fast_first_sign_in', n.get_enum_value(enablement.Enablement)),
            "idleTimeBeforeSleepInSeconds": lambda n : setattr(self, 'idle_time_before_sleep_in_seconds', n.get_int_value()),
            "kioskAppDisplayName": lambda n : setattr(self, 'kiosk_app_display_name', n.get_str_value()),
            "kioskAppUserModelId": lambda n : setattr(self, 'kiosk_app_user_model_id', n.get_str_value()),
            "localStorage": lambda n : setattr(self, 'local_storage', n.get_enum_value(enablement.Enablement)),
            "maintenanceStartTime": lambda n : setattr(self, 'maintenance_start_time', n.get_object_value(Time)),
            "setAccountManager": lambda n : setattr(self, 'set_account_manager', n.get_enum_value(enablement.Enablement)),
            "setEduPolicies": lambda n : setattr(self, 'set_edu_policies', n.get_enum_value(enablement.Enablement)),
            "setPowerPolicies": lambda n : setattr(self, 'set_power_policies', n.get_enum_value(enablement.Enablement)),
            "signInOnResume": lambda n : setattr(self, 'sign_in_on_resume', n.get_enum_value(enablement.Enablement)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def idle_time_before_sleep_in_seconds(self,) -> Optional[int]:
        """
        Gets the idleTimeBeforeSleepInSeconds property value. Specifies the time in seconds that a device must sit idle before the PC goes to sleep. Setting this value to 0 prevents the sleep timeout from occurring.
        Returns: Optional[int]
        """
        return self._idle_time_before_sleep_in_seconds
    
    @idle_time_before_sleep_in_seconds.setter
    def idle_time_before_sleep_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the idleTimeBeforeSleepInSeconds property value. Specifies the time in seconds that a device must sit idle before the PC goes to sleep. Setting this value to 0 prevents the sleep timeout from occurring.
        Args:
            value: Value to set for the idle_time_before_sleep_in_seconds property.
        """
        self._idle_time_before_sleep_in_seconds = value
    
    @property
    def kiosk_app_display_name(self,) -> Optional[str]:
        """
        Gets the kioskAppDisplayName property value. Specifies the display text for the account shown on the sign-in screen which launches the app specified by SetKioskAppUserModelId. Only applies when KioskAppUserModelId is set.
        Returns: Optional[str]
        """
        return self._kiosk_app_display_name
    
    @kiosk_app_display_name.setter
    def kiosk_app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskAppDisplayName property value. Specifies the display text for the account shown on the sign-in screen which launches the app specified by SetKioskAppUserModelId. Only applies when KioskAppUserModelId is set.
        Args:
            value: Value to set for the kiosk_app_display_name property.
        """
        self._kiosk_app_display_name = value
    
    @property
    def kiosk_app_user_model_id(self,) -> Optional[str]:
        """
        Gets the kioskAppUserModelId property value. Specifies the application user model ID of the app to use with assigned access.
        Returns: Optional[str]
        """
        return self._kiosk_app_user_model_id
    
    @kiosk_app_user_model_id.setter
    def kiosk_app_user_model_id(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskAppUserModelId property value. Specifies the application user model ID of the app to use with assigned access.
        Args:
            value: Value to set for the kiosk_app_user_model_id property.
        """
        self._kiosk_app_user_model_id = value
    
    @property
    def local_storage(self,) -> Optional[enablement.Enablement]:
        """
        Gets the localStorage property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._local_storage
    
    @local_storage.setter
    def local_storage(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the localStorage property value. Possible values of a property
        Args:
            value: Value to set for the local_storage property.
        """
        self._local_storage = value
    
    @property
    def maintenance_start_time(self,) -> Optional[Time]:
        """
        Gets the maintenanceStartTime property value. Specifies the daily start time of maintenance hour.
        Returns: Optional[Time]
        """
        return self._maintenance_start_time
    
    @maintenance_start_time.setter
    def maintenance_start_time(self,value: Optional[Time] = None) -> None:
        """
        Sets the maintenanceStartTime property value. Specifies the daily start time of maintenance hour.
        Args:
            value: Value to set for the maintenance_start_time property.
        """
        self._maintenance_start_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("accountManagerPolicy", self.account_manager_policy)
        writer.write_enum_value("allowedAccounts", self.allowed_accounts)
        writer.write_bool_value("allowLocalStorage", self.allow_local_storage)
        writer.write_bool_value("disableAccountManager", self.disable_account_manager)
        writer.write_bool_value("disableEduPolicies", self.disable_edu_policies)
        writer.write_bool_value("disablePowerPolicies", self.disable_power_policies)
        writer.write_bool_value("disableSignInOnResume", self.disable_sign_in_on_resume)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_enum_value("fastFirstSignIn", self.fast_first_sign_in)
        writer.write_int_value("idleTimeBeforeSleepInSeconds", self.idle_time_before_sleep_in_seconds)
        writer.write_str_value("kioskAppDisplayName", self.kiosk_app_display_name)
        writer.write_str_value("kioskAppUserModelId", self.kiosk_app_user_model_id)
        writer.write_enum_value("localStorage", self.local_storage)
        writer.write_object_value("maintenanceStartTime", self.maintenance_start_time)
        writer.write_enum_value("setAccountManager", self.set_account_manager)
        writer.write_enum_value("setEduPolicies", self.set_edu_policies)
        writer.write_enum_value("setPowerPolicies", self.set_power_policies)
        writer.write_enum_value("signInOnResume", self.sign_in_on_resume)
    
    @property
    def set_account_manager(self,) -> Optional[enablement.Enablement]:
        """
        Gets the setAccountManager property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._set_account_manager
    
    @set_account_manager.setter
    def set_account_manager(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the setAccountManager property value. Possible values of a property
        Args:
            value: Value to set for the set_account_manager property.
        """
        self._set_account_manager = value
    
    @property
    def set_edu_policies(self,) -> Optional[enablement.Enablement]:
        """
        Gets the setEduPolicies property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._set_edu_policies
    
    @set_edu_policies.setter
    def set_edu_policies(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the setEduPolicies property value. Possible values of a property
        Args:
            value: Value to set for the set_edu_policies property.
        """
        self._set_edu_policies = value
    
    @property
    def set_power_policies(self,) -> Optional[enablement.Enablement]:
        """
        Gets the setPowerPolicies property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._set_power_policies
    
    @set_power_policies.setter
    def set_power_policies(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the setPowerPolicies property value. Possible values of a property
        Args:
            value: Value to set for the set_power_policies property.
        """
        self._set_power_policies = value
    
    @property
    def sign_in_on_resume(self,) -> Optional[enablement.Enablement]:
        """
        Gets the signInOnResume property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._sign_in_on_resume
    
    @sign_in_on_resume.setter
    def sign_in_on_resume(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the signInOnResume property value. Possible values of a property
        Args:
            value: Value to set for the sign_in_on_resume property.
        """
        self._sign_in_on_resume = value
    

