from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

custom_extension_data = lazy_import('msgraph.generated.models.custom_extension_data')
custom_task_extension_operation_status = lazy_import('msgraph.generated.models.identity_governance.custom_task_extension_operation_status')

class CustomTaskExtensionCallbackData(custom_extension_data.CustomExtensionData):
    def __init__(self,) -> None:
        """
        Instantiates a new CustomTaskExtensionCallbackData and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.identityGovernance.customTaskExtensionCallbackData"
        # Operation status that's provided by the Azure Logic App indicating whenever the Azure Logic App has run successfully or not. Supported values: completed, failed, unknownFutureValue.
        self._operation_status: Optional[custom_task_extension_operation_status.CustomTaskExtensionOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomTaskExtensionCallbackData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomTaskExtensionCallbackData
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomTaskExtensionCallbackData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "operation_status": lambda n : setattr(self, 'operation_status', n.get_enum_value(custom_task_extension_operation_status.CustomTaskExtensionOperationStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def operation_status(self,) -> Optional[custom_task_extension_operation_status.CustomTaskExtensionOperationStatus]:
        """
        Gets the operationStatus property value. Operation status that's provided by the Azure Logic App indicating whenever the Azure Logic App has run successfully or not. Supported values: completed, failed, unknownFutureValue.
        Returns: Optional[custom_task_extension_operation_status.CustomTaskExtensionOperationStatus]
        """
        return self._operation_status
    
    @operation_status.setter
    def operation_status(self,value: Optional[custom_task_extension_operation_status.CustomTaskExtensionOperationStatus] = None) -> None:
        """
        Sets the operationStatus property value. Operation status that's provided by the Azure Logic App indicating whenever the Azure Logic App has run successfully or not. Supported values: completed, failed, unknownFutureValue.
        Args:
            value: Value to set for the operationStatus property.
        """
        self._operation_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("operationStatus", self.operation_status)
    

