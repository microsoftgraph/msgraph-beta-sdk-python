from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_governance.custom_task_extension_callback_configuration import CustomTaskExtensionCallbackConfiguration

@dataclass
class CustomExtensionCallbackConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The maximum duration in ISO 8601 format that Azure AD will wait for a resume action for the callout it sent to the logic app. The valid range for custom extensions in lifecycle workflows is five minutes to three hours. The valid range for custom extensions in entitlement management is between 5 minutes and 14 days. For example, PT3H refers to three hours, P3D refers to three days, PT10M refers to ten minutes.
    timeout_duration: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomExtensionCallbackConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionCallbackConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.customTaskExtensionCallbackConfiguration".casefold():
            from .identity_governance.custom_task_extension_callback_configuration import CustomTaskExtensionCallbackConfiguration

            return CustomTaskExtensionCallbackConfiguration()
        return CustomExtensionCallbackConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity_governance.custom_task_extension_callback_configuration import CustomTaskExtensionCallbackConfiguration

        from .identity_governance.custom_task_extension_callback_configuration import CustomTaskExtensionCallbackConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeoutDuration": lambda n : setattr(self, 'timeout_duration', n.get_timedelta_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_timedelta_value("timeoutDuration", self.timeout_duration)
        writer.write_additional_data_value(self.additional_data)
    

