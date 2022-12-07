from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_set = lazy_import('msgraph.generated.models.identity_set')

class CommentAction(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new commentAction and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If true, this activity was a reply to an existing comment thread.
        self._is_reply: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The identity of the user who started the comment thread.
        self._parent_author: Optional[identity_set.IdentitySet] = None
        # The identities of the users participating in this comment thread.
        self._participants: Optional[List[identity_set.IdentitySet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CommentAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CommentAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CommentAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_reply": lambda n : setattr(self, 'is_reply', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parent_author": lambda n : setattr(self, 'parent_author', n.get_object_value(identity_set.IdentitySet)),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(identity_set.IdentitySet)),
        }
        return fields
    
    @property
    def is_reply(self,) -> Optional[bool]:
        """
        Gets the isReply property value. If true, this activity was a reply to an existing comment thread.
        Returns: Optional[bool]
        """
        return self._is_reply
    
    @is_reply.setter
    def is_reply(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReply property value. If true, this activity was a reply to an existing comment thread.
        Args:
            value: Value to set for the isReply property.
        """
        self._is_reply = value
    
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
    def parent_author(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the parentAuthor property value. The identity of the user who started the comment thread.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._parent_author
    
    @parent_author.setter
    def parent_author(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the parentAuthor property value. The identity of the user who started the comment thread.
        Args:
            value: Value to set for the parentAuthor property.
        """
        self._parent_author = value
    
    @property
    def participants(self,) -> Optional[List[identity_set.IdentitySet]]:
        """
        Gets the participants property value. The identities of the users participating in this comment thread.
        Returns: Optional[List[identity_set.IdentitySet]]
        """
        return self._participants
    
    @participants.setter
    def participants(self,value: Optional[List[identity_set.IdentitySet]] = None) -> None:
        """
        Sets the participants property value. The identities of the users participating in this comment thread.
        Args:
            value: Value to set for the participants property.
        """
        self._participants = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("isReply", self.is_reply)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("parentAuthor", self.parent_author)
        writer.write_collection_of_object_values("participants", self.participants)
        writer.write_additional_data_value(self.additional_data)
    

