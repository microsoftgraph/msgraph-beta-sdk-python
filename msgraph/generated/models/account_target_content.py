from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import account_target_content_type, address_book_account_target_content, include_all_account_target_content

class AccountTargetContent(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new accountTargetContent and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The type of account target content. Possible values are: unknown,includeAll, addressBook,  unknownFutureValue.
        self._type: Optional[account_target_content_type.AccountTargetContentType] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccountTargetContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccountTargetContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.addressBookAccountTargetContent":
                from . import address_book_account_target_content

                return address_book_account_target_content.AddressBookAccountTargetContent()
            if mapping_value == "#microsoft.graph.includeAllAccountTargetContent":
                from . import include_all_account_target_content

                return include_all_account_target_content.IncludeAllAccountTargetContent()
        return AccountTargetContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import account_target_content_type, address_book_account_target_content, include_all_account_target_content

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(account_target_content_type.AccountTargetContentType)),
        }
        return fields
    
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[account_target_content_type.AccountTargetContentType]:
        """
        Gets the type property value. The type of account target content. Possible values are: unknown,includeAll, addressBook,  unknownFutureValue.
        Returns: Optional[account_target_content_type.AccountTargetContentType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[account_target_content_type.AccountTargetContentType] = None) -> None:
        """
        Sets the type property value. The type of account target content. Possible values are: unknown,includeAll, addressBook,  unknownFutureValue.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

