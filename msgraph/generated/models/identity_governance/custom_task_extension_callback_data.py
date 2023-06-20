from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import custom_task_extension_operation_status
    from .. import custom_extension_data

from .. import custom_extension_data

@dataclass
class CustomTaskExtensionCallbackData(custom_extension_data.CustomExtensionData):
    odata_type = "#microsoft.graph.identityGovernance.customTaskExtensionCallbackData"
    # Operation status that's provided by the Azure Logic App indicating whenever the Azure Logic App has run successfully or not. Supported values: completed, failed, unknownFutureValue.
    operation_status: Optional[custom_task_extension_operation_status.CustomTaskExtensionOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomTaskExtensionCallbackData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomTaskExtensionCallbackData
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CustomTaskExtensionCallbackData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import custom_task_extension_operation_status
        from .. import custom_extension_data

        from . import custom_task_extension_operation_status
        from .. import custom_extension_data

        fields: Dict[str, Callable[[Any], None]] = {
            "operationStatus": lambda n : setattr(self, 'operation_status', n.get_enum_value(custom_task_extension_operation_status.CustomTaskExtensionOperationStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("operationStatus", self.operation_status)
    

