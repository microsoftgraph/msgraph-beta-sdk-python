from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models import onenote_patch_content_command

class OnenotePatchContentPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new onenotePatchContentPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The commands property
        self._commands: Optional[List[onenote_patch_content_command.OnenotePatchContentCommand]] = None
    
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
    def commands(self,) -> Optional[List[onenote_patch_content_command.OnenotePatchContentCommand]]:
        """
        Gets the commands property value. The commands property
        Returns: Optional[List[onenote_patch_content_command.OnenotePatchContentCommand]]
        """
        return self._commands
    
    @commands.setter
    def commands(self,value: Optional[List[onenote_patch_content_command.OnenotePatchContentCommand]] = None) -> None:
        """
        Sets the commands property value. The commands property
        Args:
            value: Value to set for the commands property.
        """
        self._commands = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnenotePatchContentPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnenotePatchContentPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnenotePatchContentPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models import onenote_patch_content_command

        fields: Dict[str, Callable[[Any], None]] = {
            "commands": lambda n : setattr(self, 'commands', n.get_collection_of_object_values(onenote_patch_content_command.OnenotePatchContentCommand)),
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
        writer.write_collection_of_object_values("commands", self.commands)
        writer.write_additional_data_value(self.additional_data)
    

