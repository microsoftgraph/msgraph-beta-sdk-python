from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_enrollment_configuration import DeviceEnrollmentConfiguration

from .device_enrollment_configuration import DeviceEnrollmentConfiguration

@dataclass
class Windows10EnrollmentCompletionPageConfiguration(DeviceEnrollmentConfiguration):
    """
    Windows 10 Enrollment Status Page Configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10EnrollmentCompletionPageConfiguration"
    # Allow or block device reset on installation failure
    allow_device_reset_on_install_failure: Optional[bool] = None
    # Allow the user to continue using the device on installation failure
    allow_device_use_on_install_failure: Optional[bool] = None
    # Allow or block log collection on installation failure
    allow_log_collection_on_install_failure: Optional[bool] = None
    # Install all required apps as non blocking apps during white glove
    allow_non_blocking_app_installation: Optional[bool] = None
    # Allow the user to retry the setup on installation failure
    block_device_setup_retry_by_user: Optional[bool] = None
    # Set custom error message to show upon installation failure
    custom_error_message: Optional[str] = None
    # Only show installation progress for first user post enrollment
    disable_user_status_tracking_after_first_user: Optional[bool] = None
    # Set installation progress timeout in minutes
    install_progress_timeout_in_minutes: Optional[int] = None
    # Allows quality updates installation during OOBE
    install_quality_updates: Optional[bool] = None
    # Selected applications to track the installation status
    selected_mobile_app_ids: Optional[List[str]] = None
    # Show or hide installation progress to user
    show_installation_progress: Optional[bool] = None
    # Only show installation progress for Autopilot enrollment scenarios
    track_install_progress_for_autopilot_only: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10EnrollmentCompletionPageConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10EnrollmentCompletionPageConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Windows10EnrollmentCompletionPageConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_enrollment_configuration import DeviceEnrollmentConfiguration

        from .device_enrollment_configuration import DeviceEnrollmentConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "allowDeviceResetOnInstallFailure": lambda n : setattr(self, 'allow_device_reset_on_install_failure', n.get_bool_value()),
            "allowDeviceUseOnInstallFailure": lambda n : setattr(self, 'allow_device_use_on_install_failure', n.get_bool_value()),
            "allowLogCollectionOnInstallFailure": lambda n : setattr(self, 'allow_log_collection_on_install_failure', n.get_bool_value()),
            "allowNonBlockingAppInstallation": lambda n : setattr(self, 'allow_non_blocking_app_installation', n.get_bool_value()),
            "blockDeviceSetupRetryByUser": lambda n : setattr(self, 'block_device_setup_retry_by_user', n.get_bool_value()),
            "customErrorMessage": lambda n : setattr(self, 'custom_error_message', n.get_str_value()),
            "disableUserStatusTrackingAfterFirstUser": lambda n : setattr(self, 'disable_user_status_tracking_after_first_user', n.get_bool_value()),
            "installProgressTimeoutInMinutes": lambda n : setattr(self, 'install_progress_timeout_in_minutes', n.get_int_value()),
            "installQualityUpdates": lambda n : setattr(self, 'install_quality_updates', n.get_bool_value()),
            "selectedMobileAppIds": lambda n : setattr(self, 'selected_mobile_app_ids', n.get_collection_of_primitive_values(str)),
            "showInstallationProgress": lambda n : setattr(self, 'show_installation_progress', n.get_bool_value()),
            "trackInstallProgressForAutopilotOnly": lambda n : setattr(self, 'track_install_progress_for_autopilot_only', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
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
    

