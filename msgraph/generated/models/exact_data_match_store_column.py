from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ExactDataMatchStoreColumn(AdditionalDataHolder, Parsable):
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
        Instantiates a new exactDataMatchStoreColumn and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The ignoredDelimiters property
        self._ignored_delimiters: Optional[List[str]] = None
        # The isCaseInsensitive property
        self._is_case_insensitive: Optional[bool] = None
        # The isSearchable property
        self._is_searchable: Optional[bool] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactDataMatchStoreColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExactDataMatchStoreColumn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExactDataMatchStoreColumn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "ignored_delimiters": lambda n : setattr(self, 'ignored_delimiters', n.get_collection_of_primitive_values(str)),
            "is_case_insensitive": lambda n : setattr(self, 'is_case_insensitive', n.get_bool_value()),
            "is_searchable": lambda n : setattr(self, 'is_searchable', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def ignored_delimiters(self,) -> Optional[List[str]]:
        """
        Gets the ignoredDelimiters property value. The ignoredDelimiters property
        Returns: Optional[List[str]]
        """
        return self._ignored_delimiters
    
    @ignored_delimiters.setter
    def ignored_delimiters(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the ignoredDelimiters property value. The ignoredDelimiters property
        Args:
            value: Value to set for the ignoredDelimiters property.
        """
        self._ignored_delimiters = value
    
    @property
    def is_case_insensitive(self,) -> Optional[bool]:
        """
        Gets the isCaseInsensitive property value. The isCaseInsensitive property
        Returns: Optional[bool]
        """
        return self._is_case_insensitive
    
    @is_case_insensitive.setter
    def is_case_insensitive(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCaseInsensitive property value. The isCaseInsensitive property
        Args:
            value: Value to set for the isCaseInsensitive property.
        """
        self._is_case_insensitive = value
    
    @property
    def is_searchable(self,) -> Optional[bool]:
        """
        Gets the isSearchable property value. The isSearchable property
        Returns: Optional[bool]
        """
        return self._is_searchable
    
    @is_searchable.setter
    def is_searchable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSearchable property value. The isSearchable property
        Args:
            value: Value to set for the isSearchable property.
        """
        self._is_searchable = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
        writer.write_collection_of_primitive_values("ignoredDelimiters", self.ignored_delimiters)
        writer.write_bool_value("isCaseInsensitive", self.is_case_insensitive)
        writer.write_bool_value("isSearchable", self.is_searchable)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

