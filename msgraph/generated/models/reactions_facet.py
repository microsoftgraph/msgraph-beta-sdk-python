from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ReactionsFacet(AdditionalDataHolder, Parsable):
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
    def comment_count(self,) -> Optional[int]:
        """
        Gets the commentCount property value. Count of comments.
        Returns: Optional[int]
        """
        return self._comment_count
    
    @comment_count.setter
    def comment_count(self,value: Optional[int] = None) -> None:
        """
        Sets the commentCount property value. Count of comments.
        Args:
            value: Value to set for the commentCount property.
        """
        self._comment_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new reactionsFacet and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Count of comments.
        self._comment_count: Optional[int] = None
        # Count of likes.
        self._like_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Count of shares.
        self._share_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReactionsFacet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReactionsFacet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ReactionsFacet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "comment_count": lambda n : setattr(self, 'comment_count', n.get_int_value()),
            "like_count": lambda n : setattr(self, 'like_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "share_count": lambda n : setattr(self, 'share_count', n.get_int_value()),
        }
        return fields
    
    @property
    def like_count(self,) -> Optional[int]:
        """
        Gets the likeCount property value. Count of likes.
        Returns: Optional[int]
        """
        return self._like_count
    
    @like_count.setter
    def like_count(self,value: Optional[int] = None) -> None:
        """
        Sets the likeCount property value. Count of likes.
        Args:
            value: Value to set for the likeCount property.
        """
        self._like_count = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("commentCount", self.comment_count)
        writer.write_int_value("likeCount", self.like_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("shareCount", self.share_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def share_count(self,) -> Optional[int]:
        """
        Gets the shareCount property value. Count of shares.
        Returns: Optional[int]
        """
        return self._share_count
    
    @share_count.setter
    def share_count(self,value: Optional[int] = None) -> None:
        """
        Sets the shareCount property value. Count of shares.
        Args:
            value: Value to set for the shareCount property.
        """
        self._share_count = value
    

