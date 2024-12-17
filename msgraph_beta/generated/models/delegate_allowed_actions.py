from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DelegateAllowedActions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The joinActiveCalls property
    join_active_calls: Optional[bool] = None
    # The makeCalls property
    make_calls: Optional[bool] = None
    # The manageCallAndDelegateSettings property
    manage_call_and_delegate_settings: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The pickUpHeldCalls property
    pick_up_held_calls: Optional[bool] = None
    # The receiveCalls property
    receive_calls: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DelegateAllowedActions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DelegateAllowedActions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DelegateAllowedActions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "joinActiveCalls": lambda n : setattr(self, 'join_active_calls', n.get_bool_value()),
            "makeCalls": lambda n : setattr(self, 'make_calls', n.get_bool_value()),
            "manageCallAndDelegateSettings": lambda n : setattr(self, 'manage_call_and_delegate_settings', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pickUpHeldCalls": lambda n : setattr(self, 'pick_up_held_calls', n.get_bool_value()),
            "receiveCalls": lambda n : setattr(self, 'receive_calls', n.get_bool_value()),
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
        writer.write_bool_value("joinActiveCalls", self.join_active_calls)
        writer.write_bool_value("makeCalls", self.make_calls)
        writer.write_bool_value("manageCallAndDelegateSettings", self.manage_call_and_delegate_settings)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("pickUpHeldCalls", self.pick_up_held_calls)
        writer.write_bool_value("receiveCalls", self.receive_calls)
        writer.write_additional_data_value(self.additional_data)
    

