from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .term_store import set, term

class TermColumn(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new termColumn and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies whether the column will allow more than one value
        self._allow_multiple_values: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The parentTerm property
        self._parent_term: Optional[term.Term] = None
        # Specifies whether to display the entire term path or only the term label.
        self._show_fully_qualified_name: Optional[bool] = None
        # The termSet property
        self._term_set: Optional[set.Set] = None
    
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
    def allow_multiple_values(self,) -> Optional[bool]:
        """
        Gets the allowMultipleValues property value. Specifies whether the column will allow more than one value
        Returns: Optional[bool]
        """
        return self._allow_multiple_values
    
    @allow_multiple_values.setter
    def allow_multiple_values(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowMultipleValues property value. Specifies whether the column will allow more than one value
        Args:
            value: Value to set for the allow_multiple_values property.
        """
        self._allow_multiple_values = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TermColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TermColumn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TermColumn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .term_store import set, term

        fields: Dict[str, Callable[[Any], None]] = {
            "allowMultipleValues": lambda n : setattr(self, 'allow_multiple_values', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parentTerm": lambda n : setattr(self, 'parent_term', n.get_object_value(term.Term)),
            "showFullyQualifiedName": lambda n : setattr(self, 'show_fully_qualified_name', n.get_bool_value()),
            "termSet": lambda n : setattr(self, 'term_set', n.get_object_value(set.Set)),
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
    
    @property
    def parent_term(self,) -> Optional[term.Term]:
        """
        Gets the parentTerm property value. The parentTerm property
        Returns: Optional[term.Term]
        """
        return self._parent_term
    
    @parent_term.setter
    def parent_term(self,value: Optional[term.Term] = None) -> None:
        """
        Sets the parentTerm property value. The parentTerm property
        Args:
            value: Value to set for the parent_term property.
        """
        self._parent_term = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowMultipleValues", self.allow_multiple_values)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("parentTerm", self.parent_term)
        writer.write_bool_value("showFullyQualifiedName", self.show_fully_qualified_name)
        writer.write_object_value("termSet", self.term_set)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def show_fully_qualified_name(self,) -> Optional[bool]:
        """
        Gets the showFullyQualifiedName property value. Specifies whether to display the entire term path or only the term label.
        Returns: Optional[bool]
        """
        return self._show_fully_qualified_name
    
    @show_fully_qualified_name.setter
    def show_fully_qualified_name(self,value: Optional[bool] = None) -> None:
        """
        Sets the showFullyQualifiedName property value. Specifies whether to display the entire term path or only the term label.
        Args:
            value: Value to set for the show_fully_qualified_name property.
        """
        self._show_fully_qualified_name = value
    
    @property
    def term_set(self,) -> Optional[set.Set]:
        """
        Gets the termSet property value. The termSet property
        Returns: Optional[set.Set]
        """
        return self._term_set
    
    @term_set.setter
    def term_set(self,value: Optional[set.Set] = None) -> None:
        """
        Sets the termSet property value. The termSet property
        Args:
            value: Value to set for the term_set property.
        """
        self._term_set = value
    

