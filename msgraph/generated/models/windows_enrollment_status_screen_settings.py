from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class WindowsEnrollmentStatusScreenSettings(AdditionalDataHolder, Parsable):
    """
    Enrollment status screen setting
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
    def allow_device_use_before_profile_and_app_install_complete(self,) -> Optional[bool]:
        """
        Gets the allowDeviceUseBeforeProfileAndAppInstallComplete property value. Allow or block user to use device before profile and app installation complete
        Returns: Optional[bool]
        """
        return self._allow_device_use_before_profile_and_app_install_complete
    
    @allow_device_use_before_profile_and_app_install_complete.setter
    def allow_device_use_before_profile_and_app_install_complete(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowDeviceUseBeforeProfileAndAppInstallComplete property value. Allow or block user to use device before profile and app installation complete
        Args:
            value: Value to set for the allowDeviceUseBeforeProfileAndAppInstallComplete property.
        """
        self._allow_device_use_before_profile_and_app_install_complete = value
    
    @property
    def allow_device_use_on_install_failure(self,) -> Optional[bool]:
        """
        Gets the allowDeviceUseOnInstallFailure property value. Allow the user to continue using the device on installation failure
        Returns: Optional[bool]
        """
        return self._allow_device_use_on_install_failure
    
    @allow_device_use_on_install_failure.setter
    def allow_device_use_on_install_failure(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowDeviceUseOnInstallFailure property value. Allow the user to continue using the device on installation failure
        Args:
            value: Value to set for the allowDeviceUseOnInstallFailure property.
        """
        self._allow_device_use_on_install_failure = value
    
    @property
    def allow_log_collection_on_install_failure(self,) -> Optional[bool]:
        """
        Gets the allowLogCollectionOnInstallFailure property value. Allow or block log collection on installation failure
        Returns: Optional[bool]
        """
        return self._allow_log_collection_on_install_failure
    
    @allow_log_collection_on_install_failure.setter
    def allow_log_collection_on_install_failure(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowLogCollectionOnInstallFailure property value. Allow or block log collection on installation failure
        Args:
            value: Value to set for the allowLogCollectionOnInstallFailure property.
        """
        self._allow_log_collection_on_install_failure = value
    
    @property
    def block_device_setup_retry_by_user(self,) -> Optional[bool]:
        """
        Gets the blockDeviceSetupRetryByUser property value. Allow the user to retry the setup on installation failure
        Returns: Optional[bool]
        """
        return self._block_device_setup_retry_by_user
    
    @block_device_setup_retry_by_user.setter
    def block_device_setup_retry_by_user(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockDeviceSetupRetryByUser property value. Allow the user to retry the setup on installation failure
        Args:
            value: Value to set for the blockDeviceSetupRetryByUser property.
        """
        self._block_device_setup_retry_by_user = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsEnrollmentStatusScreenSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Allow or block user to use device before profile and app installation complete
        self._allow_device_use_before_profile_and_app_install_complete: Optional[bool] = None
        # Allow the user to continue using the device on installation failure
        self._allow_device_use_on_install_failure: Optional[bool] = None
        # Allow or block log collection on installation failure
        self._allow_log_collection_on_install_failure: Optional[bool] = None
        # Allow the user to retry the setup on installation failure
        self._block_device_setup_retry_by_user: Optional[bool] = None
        # Set custom error message to show upon installation failure
        self._custom_error_message: Optional[str] = None
        # Show or hide installation progress to user
        self._hide_installation_progress: Optional[bool] = None
        # Set installation progress timeout in minutes
        self._install_progress_timeout_in_minutes: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsEnrollmentStatusScreenSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsEnrollmentStatusScreenSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsEnrollmentStatusScreenSettings()
    
    @property
    def custom_error_message(self,) -> Optional[str]:
        """
        Gets the customErrorMessage property value. Set custom error message to show upon installation failure
        Returns: Optional[str]
        """
        return self._custom_error_message
    
    @custom_error_message.setter
    def custom_error_message(self,value: Optional[str] = None) -> None:
        """
        Sets the customErrorMessage property value. Set custom error message to show upon installation failure
        Args:
            value: Value to set for the customErrorMessage property.
        """
        self._custom_error_message = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_device_use_before_profile_and_app_install_complete": lambda n : setattr(self, 'allow_device_use_before_profile_and_app_install_complete', n.get_bool_value()),
            "allow_device_use_on_install_failure": lambda n : setattr(self, 'allow_device_use_on_install_failure', n.get_bool_value()),
            "allow_log_collection_on_install_failure": lambda n : setattr(self, 'allow_log_collection_on_install_failure', n.get_bool_value()),
            "block_device_setup_retry_by_user": lambda n : setattr(self, 'block_device_setup_retry_by_user', n.get_bool_value()),
            "custom_error_message": lambda n : setattr(self, 'custom_error_message', n.get_str_value()),
            "hide_installation_progress": lambda n : setattr(self, 'hide_installation_progress', n.get_bool_value()),
            "install_progress_timeout_in_minutes": lambda n : setattr(self, 'install_progress_timeout_in_minutes', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def hide_installation_progress(self,) -> Optional[bool]:
        """
        Gets the hideInstallationProgress property value. Show or hide installation progress to user
        Returns: Optional[bool]
        """
        return self._hide_installation_progress
    
    @hide_installation_progress.setter
    def hide_installation_progress(self,value: Optional[bool] = None) -> None:
        """
        Sets the hideInstallationProgress property value. Show or hide installation progress to user
        Args:
            value: Value to set for the hideInstallationProgress property.
        """
        self._hide_installation_progress = value
    
    @property
    def install_progress_timeout_in_minutes(self,) -> Optional[int]:
        """
        Gets the installProgressTimeoutInMinutes property value. Set installation progress timeout in minutes
        Returns: Optional[int]
        """
        return self._install_progress_timeout_in_minutes
    
    @install_progress_timeout_in_minutes.setter
    def install_progress_timeout_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the installProgressTimeoutInMinutes property value. Set installation progress timeout in minutes
        Args:
            value: Value to set for the installProgressTimeoutInMinutes property.
        """
        self._install_progress_timeout_in_minutes = value
    
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
        writer.write_bool_value("allowDeviceUseBeforeProfileAndAppInstallComplete", self.allow_device_use_before_profile_and_app_install_complete)
        writer.write_bool_value("allowDeviceUseOnInstallFailure", self.allow_device_use_on_install_failure)
        writer.write_bool_value("allowLogCollectionOnInstallFailure", self.allow_log_collection_on_install_failure)
        writer.write_bool_value("blockDeviceSetupRetryByUser", self.block_device_setup_retry_by_user)
        writer.write_str_value("customErrorMessage", self.custom_error_message)
        writer.write_bool_value("hideInstallationProgress", self.hide_installation_progress)
        writer.write_int_value("installProgressTimeoutInMinutes", self.install_progress_timeout_in_minutes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

