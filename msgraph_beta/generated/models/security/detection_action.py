from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_template import AlertTemplate
    from .organizational_scope import OrganizationalScope
    from .response_action import ResponseAction

@dataclass
class DetectionAction(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The alertTemplate property
    alert_template: Optional[AlertTemplate] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Groups to which the custom detection rule applies.
    organizational_scope: Optional[OrganizationalScope] = None
    # Actions taken on impacted assets as set in the custom detection rule.
    response_actions: Optional[List[ResponseAction]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DetectionAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DetectionAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DetectionAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_template import AlertTemplate
        from .organizational_scope import OrganizationalScope
        from .response_action import ResponseAction

        from .alert_template import AlertTemplate
        from .organizational_scope import OrganizationalScope
        from .response_action import ResponseAction

        fields: Dict[str, Callable[[Any], None]] = {
            "alertTemplate": lambda n : setattr(self, 'alert_template', n.get_object_value(AlertTemplate)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organizationalScope": lambda n : setattr(self, 'organizational_scope', n.get_object_value(OrganizationalScope)),
            "responseActions": lambda n : setattr(self, 'response_actions', n.get_collection_of_object_values(ResponseAction)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("alertTemplate", self.alert_template)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("organizationalScope", self.organizational_scope)
        writer.write_collection_of_object_values("responseActions", self.response_actions)
        writer.write_additional_data_value(self.additional_data)
    

