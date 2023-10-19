from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_permission_action_type import AndroidPermissionActionType

@dataclass
class AndroidPermissionAction(AdditionalDataHolder, BackedModel, Parsable):
    """
    Mapping between an Android app permission and the action Android should take when that permission is requested.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Android action taken when an app requests a dangerous permission.
    action: Optional[AndroidPermissionActionType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Android permission string, defined in the official Android documentation.  Example 'android.permission.READ_CONTACTS'.
    permission: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidPermissionAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidPermissionAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidPermissionAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_permission_action_type import AndroidPermissionActionType

        from .android_permission_action_type import AndroidPermissionActionType

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(AndroidPermissionActionType)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permission": lambda n : setattr(self, 'permission', n.get_str_value()),
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
        writer.write_enum_value("action", self.action)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("permission", self.permission)
        writer.write_additional_data_value(self.additional_data)
    

