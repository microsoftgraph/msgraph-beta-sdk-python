from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class AnswerKeyword(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new answerKeyword and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A collection of keywords used to trigger the search answer.
        self._keywords: Optional[List[str]] = None
        # If true, indicates that the search term contains similar words to the keywords that should trigger the search answer.
        self._match_similar_keywords: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Unique keywords that will guarantee the search answer is triggered.
        self._reserved_keywords: Optional[List[str]] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AnswerKeyword:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AnswerKeyword
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AnswerKeyword()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "keywords": lambda n : setattr(self, 'keywords', n.get_collection_of_primitive_values(str)),
            "matchSimilarKeywords": lambda n : setattr(self, 'match_similar_keywords', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reservedKeywords": lambda n : setattr(self, 'reserved_keywords', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def keywords(self,) -> Optional[List[str]]:
        """
        Gets the keywords property value. A collection of keywords used to trigger the search answer.
        Returns: Optional[List[str]]
        """
        return self._keywords
    
    @keywords.setter
    def keywords(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the keywords property value. A collection of keywords used to trigger the search answer.
        Args:
            value: Value to set for the keywords property.
        """
        self._keywords = value
    
    @property
    def match_similar_keywords(self,) -> Optional[bool]:
        """
        Gets the matchSimilarKeywords property value. If true, indicates that the search term contains similar words to the keywords that should trigger the search answer.
        Returns: Optional[bool]
        """
        return self._match_similar_keywords
    
    @match_similar_keywords.setter
    def match_similar_keywords(self,value: Optional[bool] = None) -> None:
        """
        Sets the matchSimilarKeywords property value. If true, indicates that the search term contains similar words to the keywords that should trigger the search answer.
        Args:
            value: Value to set for the match_similar_keywords property.
        """
        self._match_similar_keywords = value
    
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
    def reserved_keywords(self,) -> Optional[List[str]]:
        """
        Gets the reservedKeywords property value. Unique keywords that will guarantee the search answer is triggered.
        Returns: Optional[List[str]]
        """
        return self._reserved_keywords
    
    @reserved_keywords.setter
    def reserved_keywords(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the reservedKeywords property value. Unique keywords that will guarantee the search answer is triggered.
        Args:
            value: Value to set for the reserved_keywords property.
        """
        self._reserved_keywords = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("keywords", self.keywords)
        writer.write_bool_value("matchSimilarKeywords", self.match_similar_keywords)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("reservedKeywords", self.reserved_keywords)
        writer.write_additional_data_value(self.additional_data)
    

