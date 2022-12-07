from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

comment_action = lazy_import('msgraph.generated.models.comment_action')
create_action = lazy_import('msgraph.generated.models.create_action')
delete_action = lazy_import('msgraph.generated.models.delete_action')
edit_action = lazy_import('msgraph.generated.models.edit_action')
mention_action = lazy_import('msgraph.generated.models.mention_action')
move_action = lazy_import('msgraph.generated.models.move_action')
rename_action = lazy_import('msgraph.generated.models.rename_action')
restore_action = lazy_import('msgraph.generated.models.restore_action')
share_action = lazy_import('msgraph.generated.models.share_action')
version_action = lazy_import('msgraph.generated.models.version_action')

class ItemActionSet(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def comment(self,) -> Optional[comment_action.CommentAction]:
        """
        Gets the comment property value. A comment was added to the item.
        Returns: Optional[comment_action.CommentAction]
        """
        return self._comment
    
    @comment.setter
    def comment(self,value: Optional[comment_action.CommentAction] = None) -> None:
        """
        Sets the comment property value. A comment was added to the item.
        Args:
            value: Value to set for the comment property.
        """
        self._comment = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new itemActionSet and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A comment was added to the item.
        self._comment: Optional[comment_action.CommentAction] = None
        # An item was created.
        self._create: Optional[create_action.CreateAction] = None
        # An item was deleted.
        self._delete: Optional[delete_action.DeleteAction] = None
        # An item was edited.
        self._edit: Optional[edit_action.EditAction] = None
        # A user was mentioned in the item.
        self._mention: Optional[mention_action.MentionAction] = None
        # An item was moved.
        self._move: Optional[move_action.MoveAction] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # An item was renamed.
        self._rename: Optional[rename_action.RenameAction] = None
        # An item was restored.
        self._restore: Optional[restore_action.RestoreAction] = None
        # An item was shared.
        self._share: Optional[share_action.ShareAction] = None
        # An item was versioned.
        self._version: Optional[version_action.VersionAction] = None
    
    @property
    def create(self,) -> Optional[create_action.CreateAction]:
        """
        Gets the create property value. An item was created.
        Returns: Optional[create_action.CreateAction]
        """
        return self._create
    
    @create.setter
    def create(self,value: Optional[create_action.CreateAction] = None) -> None:
        """
        Sets the create property value. An item was created.
        Args:
            value: Value to set for the create property.
        """
        self._create = value
    
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
    
    @property
    def delete(self,) -> Optional[delete_action.DeleteAction]:
        """
        Gets the delete property value. An item was deleted.
        Returns: Optional[delete_action.DeleteAction]
        """
        return self._delete
    
    @delete.setter
    def delete(self,value: Optional[delete_action.DeleteAction] = None) -> None:
        """
        Sets the delete property value. An item was deleted.
        Args:
            value: Value to set for the delete property.
        """
        self._delete = value
    
    @property
    def edit(self,) -> Optional[edit_action.EditAction]:
        """
        Gets the edit property value. An item was edited.
        Returns: Optional[edit_action.EditAction]
        """
        return self._edit
    
    @edit.setter
    def edit(self,value: Optional[edit_action.EditAction] = None) -> None:
        """
        Sets the edit property value. An item was edited.
        Args:
            value: Value to set for the edit property.
        """
        self._edit = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
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
    
    @property
    def mention(self,) -> Optional[mention_action.MentionAction]:
        """
        Gets the mention property value. A user was mentioned in the item.
        Returns: Optional[mention_action.MentionAction]
        """
        return self._mention
    
    @mention.setter
    def mention(self,value: Optional[mention_action.MentionAction] = None) -> None:
        """
        Sets the mention property value. A user was mentioned in the item.
        Args:
            value: Value to set for the mention property.
        """
        self._mention = value
    
    @property
    def move(self,) -> Optional[move_action.MoveAction]:
        """
        Gets the move property value. An item was moved.
        Returns: Optional[move_action.MoveAction]
        """
        return self._move
    
    @move.setter
    def move(self,value: Optional[move_action.MoveAction] = None) -> None:
        """
        Sets the move property value. An item was moved.
        Args:
            value: Value to set for the move property.
        """
        self._move = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def rename(self,) -> Optional[rename_action.RenameAction]:
        """
        Gets the rename property value. An item was renamed.
        Returns: Optional[rename_action.RenameAction]
        """
        return self._rename
    
    @rename.setter
    def rename(self,value: Optional[rename_action.RenameAction] = None) -> None:
        """
        Sets the rename property value. An item was renamed.
        Args:
            value: Value to set for the rename property.
        """
        self._rename = value
    
    @property
    def restore(self,) -> Optional[restore_action.RestoreAction]:
        """
        Gets the restore property value. An item was restored.
        Returns: Optional[restore_action.RestoreAction]
        """
        return self._restore
    
    @restore.setter
    def restore(self,value: Optional[restore_action.RestoreAction] = None) -> None:
        """
        Sets the restore property value. An item was restored.
        Args:
            value: Value to set for the restore property.
        """
        self._restore = value
    
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
    
    @property
    def share(self,) -> Optional[share_action.ShareAction]:
        """
        Gets the share property value. An item was shared.
        Returns: Optional[share_action.ShareAction]
        """
        return self._share
    
    @share.setter
    def share(self,value: Optional[share_action.ShareAction] = None) -> None:
        """
        Sets the share property value. An item was shared.
        Args:
            value: Value to set for the share property.
        """
        self._share = value
    
    @property
    def version(self,) -> Optional[version_action.VersionAction]:
        """
        Gets the version property value. An item was versioned.
        Returns: Optional[version_action.VersionAction]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[version_action.VersionAction] = None) -> None:
        """
        Sets the version property value. An item was versioned.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

