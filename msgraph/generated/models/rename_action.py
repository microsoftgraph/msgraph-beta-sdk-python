from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class RenameAction(AdditionalDataHolder, Parsable):
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
        Instantiates a new renameAction and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The new name of the item.
        self._new_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The previous name of the item.
        self._old_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RenameAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RenameAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RenameAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "new_name": lambda n : setattr(self, 'new_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "old_name": lambda n : setattr(self, 'old_name', n.get_str_value()),
        }
        return fields
    
    @property
    def new_name(self,) -> Optional[str]:
        """
        Gets the newName property value. The new name of the item.
        Returns: Optional[str]
        """
        return self._new_name
    
    @new_name.setter
    def new_name(self,value: Optional[str] = None) -> None:
        """
        Sets the newName property value. The new name of the item.
        Args:
            value: Value to set for the newName property.
        """
        self._new_name = value
    
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
    def old_name(self,) -> Optional[str]:
        """
        Gets the oldName property value. The previous name of the item.
        Returns: Optional[str]
        """
        return self._old_name
    
    @old_name.setter
    def old_name(self,value: Optional[str] = None) -> None:
        """
        Sets the oldName property value. The previous name of the item.
        Args:
            value: Value to set for the oldName property.
        """
        self._old_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("newName", self.new_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("oldName", self.old_name)
        writer.write_additional_data_value(self.additional_data)
    

