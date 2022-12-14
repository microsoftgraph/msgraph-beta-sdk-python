from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_enrollment_configuration = lazy_import('msgraph.generated.models.device_enrollment_configuration')
enrollment_notification_branding_options = lazy_import('msgraph.generated.models.enrollment_notification_branding_options')
enrollment_notification_template_type = lazy_import('msgraph.generated.models.enrollment_notification_template_type')
enrollment_restriction_platform_type = lazy_import('msgraph.generated.models.enrollment_restriction_platform_type')

class DeviceEnrollmentNotificationConfiguration(device_enrollment_configuration.DeviceEnrollmentConfiguration):
    @property
    def branding_options(self,) -> Optional[enrollment_notification_branding_options.EnrollmentNotificationBrandingOptions]:
        """
        Gets the brandingOptions property value. Branding Options for the Message Template. Branding is defined in the Intune Admin Console.
        Returns: Optional[enrollment_notification_branding_options.EnrollmentNotificationBrandingOptions]
        """
        return self._branding_options
    
    @branding_options.setter
    def branding_options(self,value: Optional[enrollment_notification_branding_options.EnrollmentNotificationBrandingOptions] = None) -> None:
        """
        Sets the brandingOptions property value. Branding Options for the Message Template. Branding is defined in the Intune Admin Console.
        Args:
            value: Value to set for the brandingOptions property.
        """
        self._branding_options = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceEnrollmentNotificationConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceEnrollmentNotificationConfiguration"
        # Branding Options for the Message Template. Branding is defined in the Intune Admin Console.
        self._branding_options: Optional[enrollment_notification_branding_options.EnrollmentNotificationBrandingOptions] = None
        # DefaultLocale for the Enrollment Notification
        self._default_locale: Optional[str] = None
        # Notification Message Template Id
        self._notification_message_template_id: Optional[Guid] = None
        # The list of notification data -
        self._notification_templates: Optional[List[str]] = None
        # This enum indicates the platform type for which the enrollment restriction applies.
        self._platform_type: Optional[enrollment_restriction_platform_type.EnrollmentRestrictionPlatformType] = None
        # This enum indicates the Template type for which the enrollment notification applies.
        self._template_type: Optional[enrollment_notification_template_type.EnrollmentNotificationTemplateType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceEnrollmentNotificationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentNotificationConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceEnrollmentNotificationConfiguration()
    
    @property
    def default_locale(self,) -> Optional[str]:
        """
        Gets the defaultLocale property value. DefaultLocale for the Enrollment Notification
        Returns: Optional[str]
        """
        return self._default_locale
    
    @default_locale.setter
    def default_locale(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultLocale property value. DefaultLocale for the Enrollment Notification
        Args:
            value: Value to set for the defaultLocale property.
        """
        self._default_locale = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "branding_options": lambda n : setattr(self, 'branding_options', n.get_enum_value(enrollment_notification_branding_options.EnrollmentNotificationBrandingOptions)),
            "default_locale": lambda n : setattr(self, 'default_locale', n.get_str_value()),
            "notification_message_template_id": lambda n : setattr(self, 'notification_message_template_id', n.get_object_value(Guid)),
            "notification_templates": lambda n : setattr(self, 'notification_templates', n.get_collection_of_primitive_values(str)),
            "platform_type": lambda n : setattr(self, 'platform_type', n.get_enum_value(enrollment_restriction_platform_type.EnrollmentRestrictionPlatformType)),
            "template_type": lambda n : setattr(self, 'template_type', n.get_enum_value(enrollment_notification_template_type.EnrollmentNotificationTemplateType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def notification_message_template_id(self,) -> Optional[Guid]:
        """
        Gets the notificationMessageTemplateId property value. Notification Message Template Id
        Returns: Optional[Guid]
        """
        return self._notification_message_template_id
    
    @notification_message_template_id.setter
    def notification_message_template_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the notificationMessageTemplateId property value. Notification Message Template Id
        Args:
            value: Value to set for the notificationMessageTemplateId property.
        """
        self._notification_message_template_id = value
    
    @property
    def notification_templates(self,) -> Optional[List[str]]:
        """
        Gets the notificationTemplates property value. The list of notification data -
        Returns: Optional[List[str]]
        """
        return self._notification_templates
    
    @notification_templates.setter
    def notification_templates(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the notificationTemplates property value. The list of notification data -
        Args:
            value: Value to set for the notificationTemplates property.
        """
        self._notification_templates = value
    
    @property
    def platform_type(self,) -> Optional[enrollment_restriction_platform_type.EnrollmentRestrictionPlatformType]:
        """
        Gets the platformType property value. This enum indicates the platform type for which the enrollment restriction applies.
        Returns: Optional[enrollment_restriction_platform_type.EnrollmentRestrictionPlatformType]
        """
        return self._platform_type
    
    @platform_type.setter
    def platform_type(self,value: Optional[enrollment_restriction_platform_type.EnrollmentRestrictionPlatformType] = None) -> None:
        """
        Sets the platformType property value. This enum indicates the platform type for which the enrollment restriction applies.
        Args:
            value: Value to set for the platformType property.
        """
        self._platform_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("brandingOptions", self.branding_options)
        writer.write_str_value("defaultLocale", self.default_locale)
        writer.write_object_value("notificationMessageTemplateId", self.notification_message_template_id)
        writer.write_collection_of_primitive_values("notificationTemplates", self.notification_templates)
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_enum_value("templateType", self.template_type)
    
    @property
    def template_type(self,) -> Optional[enrollment_notification_template_type.EnrollmentNotificationTemplateType]:
        """
        Gets the templateType property value. This enum indicates the Template type for which the enrollment notification applies.
        Returns: Optional[enrollment_notification_template_type.EnrollmentNotificationTemplateType]
        """
        return self._template_type
    
    @template_type.setter
    def template_type(self,value: Optional[enrollment_notification_template_type.EnrollmentNotificationTemplateType] = None) -> None:
        """
        Sets the templateType property value. This enum indicates the Template type for which the enrollment notification applies.
        Args:
            value: Value to set for the templateType property.
        """
        self._template_type = value
    

