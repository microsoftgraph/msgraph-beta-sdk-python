from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_enrollment_configuration = lazy_import('msgraph.generated.models.device_enrollment_configuration')

class Windows10EnrollmentCompletionPageConfiguration(device_enrollment_configuration.DeviceEnrollmentConfiguration):
    @property
    def allow_device_reset_on_install_failure(self,) -> Optional[bool]:
        """
        Gets the allowDeviceResetOnInstallFailure property value. Allow or block device reset on installation failure
        Returns: Optional[bool]
        """
        return self._allow_device_reset_on_install_failure
    
    @allow_device_reset_on_install_failure.setter
    def allow_device_reset_on_install_failure(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowDeviceResetOnInstallFailure property value. Allow or block device reset on installation failure
        Args:
            value: Value to set for the allowDeviceResetOnInstallFailure property.
        """
        self._allow_device_reset_on_install_failure = value
    
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
    def allow_non_blocking_app_installation(self,) -> Optional[bool]:
        """
        Gets the allowNonBlockingAppInstallation property value. Install all required apps as non blocking apps during white glove
        Returns: Optional[bool]
        """
        return self._allow_non_blocking_app_installation
    
    @allow_non_blocking_app_installation.setter
    def allow_non_blocking_app_installation(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowNonBlockingAppInstallation property value. Install all required apps as non blocking apps during white glove
        Args:
            value: Value to set for the allowNonBlockingAppInstallation property.
        """
        self._allow_non_blocking_app_installation = value
    
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
        Instantiates a new Windows10EnrollmentCompletionPageConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10EnrollmentCompletionPageConfiguration"
        # Allow or block device reset on installation failure
        self._allow_device_reset_on_install_failure: Optional[bool] = None
        # Allow the user to continue using the device on installation failure
        self._allow_device_use_on_install_failure: Optional[bool] = None
        # Allow or block log collection on installation failure
        self._allow_log_collection_on_install_failure: Optional[bool] = None
        # Install all required apps as non blocking apps during white glove
        self._allow_non_blocking_app_installation: Optional[bool] = None
        # Allow the user to retry the setup on installation failure
        self._block_device_setup_retry_by_user: Optional[bool] = None
        # Set custom error message to show upon installation failure
        self._custom_error_message: Optional[str] = None
        # Only show installation progress for first user post enrollment
        self._disable_user_status_tracking_after_first_user: Optional[bool] = None
        # Set installation progress timeout in minutes
        self._install_progress_timeout_in_minutes: Optional[int] = None
        # Allows quality updates installation during OOBE
        self._install_quality_updates: Optional[bool] = None
        # Selected applications to track the installation status
        self._selected_mobile_app_ids: Optional[List[str]] = None
        # Show or hide installation progress to user
        self._show_installation_progress: Optional[bool] = None
        # Only show installation progress for Autopilot enrollment scenarios
        self._track_install_progress_for_autopilot_only: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10EnrollmentCompletionPageConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10EnrollmentCompletionPageConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10EnrollmentCompletionPageConfiguration()
    
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
    
    @property
    def disable_user_status_tracking_after_first_user(self,) -> Optional[bool]:
        """
        Gets the disableUserStatusTrackingAfterFirstUser property value. Only show installation progress for first user post enrollment
        Returns: Optional[bool]
        """
        return self._disable_user_status_tracking_after_first_user
    
    @disable_user_status_tracking_after_first_user.setter
    def disable_user_status_tracking_after_first_user(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableUserStatusTrackingAfterFirstUser property value. Only show installation progress for first user post enrollment
        Args:
            value: Value to set for the disableUserStatusTrackingAfterFirstUser property.
        """
        self._disable_user_status_tracking_after_first_user = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_device_reset_on_install_failure": lambda n : setattr(self, 'allow_device_reset_on_install_failure', n.get_bool_value()),
            "allow_device_use_on_install_failure": lambda n : setattr(self, 'allow_device_use_on_install_failure', n.get_bool_value()),
            "allow_log_collection_on_install_failure": lambda n : setattr(self, 'allow_log_collection_on_install_failure', n.get_bool_value()),
            "allow_non_blocking_app_installation": lambda n : setattr(self, 'allow_non_blocking_app_installation', n.get_bool_value()),
            "block_device_setup_retry_by_user": lambda n : setattr(self, 'block_device_setup_retry_by_user', n.get_bool_value()),
            "custom_error_message": lambda n : setattr(self, 'custom_error_message', n.get_str_value()),
            "disable_user_status_tracking_after_first_user": lambda n : setattr(self, 'disable_user_status_tracking_after_first_user', n.get_bool_value()),
            "install_progress_timeout_in_minutes": lambda n : setattr(self, 'install_progress_timeout_in_minutes', n.get_int_value()),
            "install_quality_updates": lambda n : setattr(self, 'install_quality_updates', n.get_bool_value()),
            "selected_mobile_app_ids": lambda n : setattr(self, 'selected_mobile_app_ids', n.get_collection_of_primitive_values(str)),
            "show_installation_progress": lambda n : setattr(self, 'show_installation_progress', n.get_bool_value()),
            "track_install_progress_for_autopilot_only": lambda n : setattr(self, 'track_install_progress_for_autopilot_only', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    def install_quality_updates(self,) -> Optional[bool]:
        """
        Gets the installQualityUpdates property value. Allows quality updates installation during OOBE
        Returns: Optional[bool]
        """
        return self._install_quality_updates
    
    @install_quality_updates.setter
    def install_quality_updates(self,value: Optional[bool] = None) -> None:
        """
        Sets the installQualityUpdates property value. Allows quality updates installation during OOBE
        Args:
            value: Value to set for the installQualityUpdates property.
        """
        self._install_quality_updates = value
    
    @property
    def selected_mobile_app_ids(self,) -> Optional[List[str]]:
        """
        Gets the selectedMobileAppIds property value. Selected applications to track the installation status
        Returns: Optional[List[str]]
        """
        return self._selected_mobile_app_ids
    
    @selected_mobile_app_ids.setter
    def selected_mobile_app_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the selectedMobileAppIds property value. Selected applications to track the installation status
        Args:
            value: Value to set for the selectedMobileAppIds property.
        """
        self._selected_mobile_app_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowDeviceResetOnInstallFailure", self.allow_device_reset_on_install_failure)
        writer.write_bool_value("allowDeviceUseOnInstallFailure", self.allow_device_use_on_install_failure)
        writer.write_bool_value("allowLogCollectionOnInstallFailure", self.allow_log_collection_on_install_failure)
        writer.write_bool_value("allowNonBlockingAppInstallation", self.allow_non_blocking_app_installation)
        writer.write_bool_value("blockDeviceSetupRetryByUser", self.block_device_setup_retry_by_user)
        writer.write_str_value("customErrorMessage", self.custom_error_message)
        writer.write_bool_value("disableUserStatusTrackingAfterFirstUser", self.disable_user_status_tracking_after_first_user)
        writer.write_int_value("installProgressTimeoutInMinutes", self.install_progress_timeout_in_minutes)
        writer.write_bool_value("installQualityUpdates", self.install_quality_updates)
        writer.write_collection_of_primitive_values("selectedMobileAppIds", self.selected_mobile_app_ids)
        writer.write_bool_value("showInstallationProgress", self.show_installation_progress)
        writer.write_bool_value("trackInstallProgressForAutopilotOnly", self.track_install_progress_for_autopilot_only)
    
    @property
    def show_installation_progress(self,) -> Optional[bool]:
        """
        Gets the showInstallationProgress property value. Show or hide installation progress to user
        Returns: Optional[bool]
        """
        return self._show_installation_progress
    
    @show_installation_progress.setter
    def show_installation_progress(self,value: Optional[bool] = None) -> None:
        """
        Sets the showInstallationProgress property value. Show or hide installation progress to user
        Args:
            value: Value to set for the showInstallationProgress property.
        """
        self._show_installation_progress = value
    
    @property
    def track_install_progress_for_autopilot_only(self,) -> Optional[bool]:
        """
        Gets the trackInstallProgressForAutopilotOnly property value. Only show installation progress for Autopilot enrollment scenarios
        Returns: Optional[bool]
        """
        return self._track_install_progress_for_autopilot_only
    
    @track_install_progress_for_autopilot_only.setter
    def track_install_progress_for_autopilot_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the trackInstallProgressForAutopilotOnly property value. Only show installation progress for Autopilot enrollment scenarios
        Args:
            value: Value to set for the trackInstallProgressForAutopilotOnly property.
        """
        self._track_install_progress_for_autopilot_only = value
    

