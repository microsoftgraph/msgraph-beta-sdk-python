from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import comment_action, create_action, delete_action, edit_action, mention_action, move_action, rename_action, restore_action, share_action, version_action

@dataclass
class ItemActionSet(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # A comment was added to the item.
    comment: Optional[comment_action.CommentAction] = None
    # An item was created.
    create: Optional[create_action.CreateAction] = None
    # An item was deleted.
    delete: Optional[delete_action.DeleteAction] = None
    # An item was edited.
    edit: Optional[edit_action.EditAction] = None
    # A user was mentioned in the item.
    mention: Optional[mention_action.MentionAction] = None
    # An item was moved.
    move: Optional[move_action.MoveAction] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # An item was renamed.
    rename: Optional[rename_action.RenameAction] = None
    # An item was restored.
    restore: Optional[restore_action.RestoreAction] = None
    # An item was shared.
    share: Optional[share_action.ShareAction] = None
    # An item was versioned.
    version: Optional[version_action.VersionAction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemActionSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemActionSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemActionSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import comment_action, create_action, delete_action, edit_action, mention_action, move_action, rename_action, restore_action, share_action, version_action

        fields: Dict[str, Callable[[Any], None]] = {
            "comment": lambda n : setattr(self, 'comment', n.get_object_value(comment_action.CommentAction)),
            "create": lambda n : setattr(self, 'create', n.get_object_value(create_action.CreateAction)),
            "delete": lambda n : setattr(self, 'delete', n.get_object_value(delete_action.DeleteAction)),
            "edit": lambda n : setattr(self, 'edit', n.get_object_value(edit_action.EditAction)),
            "mention": lambda n : setattr(self, 'mention', n.get_object_value(mention_action.MentionAction)),
            "move": lambda n : setattr(self, 'move', n.get_object_value(move_action.MoveAction)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rename": lambda n : setattr(self, 'rename', n.get_object_value(rename_action.RenameAction)),
            "restore": lambda n : setattr(self, 'restore', n.get_object_value(restore_action.RestoreAction)),
            "share": lambda n : setattr(self, 'share', n.get_object_value(share_action.ShareAction)),
            "version": lambda n : setattr(self, 'version', n.get_object_value(version_action.VersionAction)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("comment", self.comment)
        writer.write_object_value("create", self.create)
        writer.write_object_value("delete", self.delete)
        writer.write_object_value("edit", self.edit)
        writer.write_object_value("mention", self.mention)
        writer.write_object_value("move", self.move)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("rename", self.rename)
        writer.write_object_value("restore", self.restore)
        writer.write_object_value("share", self.share)
        writer.write_object_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

