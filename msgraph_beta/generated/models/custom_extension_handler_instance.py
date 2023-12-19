from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_extension_handler_instance_stage import CustomExtensionHandlerInstance_stage
    from .custom_extension_handler_instance_status import CustomExtensionHandlerInstance_status

@dataclass
class CustomExtensionHandlerInstance(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Identifier of the customAccessPackageWorkflowExtension triggered at this instance.
    custom_extension_id: Optional[str] = None
    # The unique run ID for the logic app.
    external_correlation_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the stage of the request workflow when the access package custom extension runs. The possible values are: assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue.
    stage: Optional[CustomExtensionHandlerInstance_stage] = None
    # Status of the request to run the access package custom extension workflow that is associated with the logic app. The possible values are: requestSent, requestReceived, unknownFutureValue.
    status: Optional[CustomExtensionHandlerInstance_status] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomExtensionHandlerInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionHandlerInstance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CustomExtensionHandlerInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_extension_handler_instance_stage import CustomExtensionHandlerInstance_stage
        from .custom_extension_handler_instance_status import CustomExtensionHandlerInstance_status

        from .custom_extension_handler_instance_stage import CustomExtensionHandlerInstance_stage
        from .custom_extension_handler_instance_status import CustomExtensionHandlerInstance_status

        fields: Dict[str, Callable[[Any], None]] = {
            "customExtensionId": lambda n : setattr(self, 'custom_extension_id', n.get_str_value()),
            "externalCorrelationId": lambda n : setattr(self, 'external_correlation_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(CustomExtensionHandlerInstance_stage)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CustomExtensionHandlerInstance_status)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("customExtensionId", self.custom_extension_id)
        writer.write_str_value("externalCorrelationId", self.external_correlation_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("stage", self.stage)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

