from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

label = lazy_import('msgraph.generated.models.label')
property_type = lazy_import('msgraph.generated.models.property_type')

class Property(AdditionalDataHolder, Parsable):
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
    def aliases(self,) -> Optional[List[str]]:
        """
        Gets the aliases property value. The aliases property
        Returns: Optional[List[str]]
        """
        return self._aliases
    
    @aliases.setter
    def aliases(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the aliases property value. The aliases property
        Args:
            value: Value to set for the aliases property.
        """
        self._aliases = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new property and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The aliases property
        self._aliases: Optional[List[str]] = None
        # The isQueryable property
        self._is_queryable: Optional[bool] = None
        # The isRefinable property
        self._is_refinable: Optional[bool] = None
        # The isRetrievable property
        self._is_retrievable: Optional[bool] = None
        # The isSearchable property
        self._is_searchable: Optional[bool] = None
        # The labels property
        self._labels: Optional[List[label.Label]] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The type property
        self._type: Optional[property_type.PropertyType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Property:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Property
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Property()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "aliases": lambda n : setattr(self, 'aliases', n.get_collection_of_primitive_values(str)),
            "is_queryable": lambda n : setattr(self, 'is_queryable', n.get_bool_value()),
            "is_refinable": lambda n : setattr(self, 'is_refinable', n.get_bool_value()),
            "is_retrievable": lambda n : setattr(self, 'is_retrievable', n.get_bool_value()),
            "is_searchable": lambda n : setattr(self, 'is_searchable', n.get_bool_value()),
            "labels": lambda n : setattr(self, 'labels', n.get_collection_of_enum_values(label.Label)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(property_type.PropertyType)),
        }
        return fields
    
    @property
    def is_queryable(self,) -> Optional[bool]:
        """
        Gets the isQueryable property value. The isQueryable property
        Returns: Optional[bool]
        """
        return self._is_queryable
    
    @is_queryable.setter
    def is_queryable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isQueryable property value. The isQueryable property
        Args:
            value: Value to set for the isQueryable property.
        """
        self._is_queryable = value
    
    @property
    def is_refinable(self,) -> Optional[bool]:
        """
        Gets the isRefinable property value. The isRefinable property
        Returns: Optional[bool]
        """
        return self._is_refinable
    
    @is_refinable.setter
    def is_refinable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRefinable property value. The isRefinable property
        Args:
            value: Value to set for the isRefinable property.
        """
        self._is_refinable = value
    
    @property
    def is_retrievable(self,) -> Optional[bool]:
        """
        Gets the isRetrievable property value. The isRetrievable property
        Returns: Optional[bool]
        """
        return self._is_retrievable
    
    @is_retrievable.setter
    def is_retrievable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRetrievable property value. The isRetrievable property
        Args:
            value: Value to set for the isRetrievable property.
        """
        self._is_retrievable = value
    
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
    def labels(self,) -> Optional[List[label.Label]]:
        """
        Gets the labels property value. The labels property
        Returns: Optional[List[label.Label]]
        """
        return self._labels
    
    @labels.setter
    def labels(self,value: Optional[List[label.Label]] = None) -> None:
        """
        Sets the labels property value. The labels property
        Args:
            value: Value to set for the labels property.
        """
        self._labels = value
    
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
        writer.write_collection_of_primitive_values("aliases", self.aliases)
        writer.write_bool_value("isQueryable", self.is_queryable)
        writer.write_bool_value("isRefinable", self.is_refinable)
        writer.write_bool_value("isRetrievable", self.is_retrievable)
        writer.write_bool_value("isSearchable", self.is_searchable)
        writer.write_enum_value("labels", self.labels)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[property_type.PropertyType]:
        """
        Gets the type property value. The type property
        Returns: Optional[property_type.PropertyType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[property_type.PropertyType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

