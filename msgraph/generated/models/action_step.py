from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_url import ActionUrl

@dataclass
class ActionStep(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # A link to the documentation or Microsoft Entra admin center page that is associated with the action step.
    action_url: Optional[ActionUrl] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the position for this action in the order of the collection of actions to be taken.
    step_number: Optional[int] = None
    # Friendly description of the action to take.
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ActionStep:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActionStep
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ActionStep()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .action_url import ActionUrl

        from .action_url import ActionUrl

        fields: Dict[str, Callable[[Any], None]] = {
            "actionUrl": lambda n : setattr(self, 'action_url', n.get_object_value(ActionUrl)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "stepNumber": lambda n : setattr(self, 'step_number', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_object_value("actionUrl", self.action_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("stepNumber", self.step_number)
        writer.write_str_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    

