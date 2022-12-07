from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

governance_notification_template = lazy_import('msgraph.generated.models.governance_notification_template')

class GovernanceNotificationPolicy(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new governanceNotificationPolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The enabledTemplateTypes property
        self._enabled_template_types: Optional[List[str]] = None
        # The notificationTemplates property
        self._notification_templates: Optional[List[governance_notification_template.GovernanceNotificationTemplate]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GovernanceNotificationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceNotificationPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GovernanceNotificationPolicy()
    
    @property
    def enabled_template_types(self,) -> Optional[List[str]]:
        """
        Gets the enabledTemplateTypes property value. The enabledTemplateTypes property
        Returns: Optional[List[str]]
        """
        return self._enabled_template_types
    
    @enabled_template_types.setter
    def enabled_template_types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enabledTemplateTypes property value. The enabledTemplateTypes property
        Args:
            value: Value to set for the enabledTemplateTypes property.
        """
        self._enabled_template_types = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enabled_template_types": lambda n : setattr(self, 'enabled_template_types', n.get_collection_of_primitive_values(str)),
            "notification_templates": lambda n : setattr(self, 'notification_templates', n.get_collection_of_object_values(governance_notification_template.GovernanceNotificationTemplate)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def notification_templates(self,) -> Optional[List[governance_notification_template.GovernanceNotificationTemplate]]:
        """
        Gets the notificationTemplates property value. The notificationTemplates property
        Returns: Optional[List[governance_notification_template.GovernanceNotificationTemplate]]
        """
        return self._notification_templates
    
    @notification_templates.setter
    def notification_templates(self,value: Optional[List[governance_notification_template.GovernanceNotificationTemplate]] = None) -> None:
        """
        Sets the notificationTemplates property value. The notificationTemplates property
        Args:
            value: Value to set for the notificationTemplates property.
        """
        self._notification_templates = value
    
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
        writer.write_collection_of_primitive_values("enabledTemplateTypes", self.enabled_template_types)
        writer.write_collection_of_object_values("notificationTemplates", self.notification_templates)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

