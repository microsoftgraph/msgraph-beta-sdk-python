from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

email_address = lazy_import('msgraph.generated.models.email_address')
email_type = lazy_import('msgraph.generated.models.email_type')

class TypedEmailAddress(email_address.EmailAddress):
    def __init__(self,) -> None:
        """
        Instantiates a new TypedEmailAddress and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.typedEmailAddress"
        # To specify a custom type of email address, set type to other, and assign otherLabel to a custom string. For example, you may use a specific email address for your volunteer activities. Set type to other, and set otherLabel to a custom string such as Volunteer work.
        self._other_label: Optional[str] = None
        # The type of email address. Possible values are: unknown, work, personal, main, other. The default value is unknown, which means address has not been set as a specific type.
        self._type: Optional[email_type.EmailType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TypedEmailAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TypedEmailAddress
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TypedEmailAddress()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "other_label": lambda n : setattr(self, 'other_label', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(email_type.EmailType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def other_label(self,) -> Optional[str]:
        """
        Gets the otherLabel property value. To specify a custom type of email address, set type to other, and assign otherLabel to a custom string. For example, you may use a specific email address for your volunteer activities. Set type to other, and set otherLabel to a custom string such as Volunteer work.
        Returns: Optional[str]
        """
        return self._other_label
    
    @other_label.setter
    def other_label(self,value: Optional[str] = None) -> None:
        """
        Sets the otherLabel property value. To specify a custom type of email address, set type to other, and assign otherLabel to a custom string. For example, you may use a specific email address for your volunteer activities. Set type to other, and set otherLabel to a custom string such as Volunteer work.
        Args:
            value: Value to set for the otherLabel property.
        """
        self._other_label = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("otherLabel", self.other_label)
        writer.write_enum_value("type", self.type)
    
    @property
    def type(self,) -> Optional[email_type.EmailType]:
        """
        Gets the type property value. The type of email address. Possible values are: unknown, work, personal, main, other. The default value is unknown, which means address has not been set as a specific type.
        Returns: Optional[email_type.EmailType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[email_type.EmailType] = None) -> None:
        """
        Sets the type property value. The type of email address. Possible values are: unknown, work, personal, main, other. The default value is unknown, which means address has not been set as a specific type.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

