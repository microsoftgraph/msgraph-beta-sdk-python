from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_management_configuration import AppManagementConfiguration
    from .custom_app_management_application_configuration import CustomAppManagementApplicationConfiguration

from .app_management_configuration import AppManagementConfiguration

@dataclass
class CustomAppManagementConfiguration(AppManagementConfiguration):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customAppManagementConfiguration"
    # Restrictions applicable only to application objects that the policy applies to.
    application_restrictions: Optional[CustomAppManagementApplicationConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomAppManagementConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomAppManagementConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomAppManagementConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_management_configuration import AppManagementConfiguration
        from .custom_app_management_application_configuration import CustomAppManagementApplicationConfiguration

        from .app_management_configuration import AppManagementConfiguration
        from .custom_app_management_application_configuration import CustomAppManagementApplicationConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationRestrictions": lambda n : setattr(self, 'application_restrictions', n.get_object_value(CustomAppManagementApplicationConfiguration)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("applicationRestrictions", self.application_restrictions)
    

