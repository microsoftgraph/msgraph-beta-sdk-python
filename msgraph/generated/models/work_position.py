from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_facet = lazy_import('msgraph.generated.models.item_facet')
position_detail = lazy_import('msgraph.generated.models.position_detail')
related_person = lazy_import('msgraph.generated.models.related_person')

class WorkPosition(item_facet.ItemFacet):
    @property
    def categories(self,) -> Optional[List[str]]:
        """
        Gets the categories property value. Categories that the user has associated with this position.
        Returns: Optional[List[str]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the categories property value. Categories that the user has associated with this position.
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    @property
    def colleagues(self,) -> Optional[List[related_person.RelatedPerson]]:
        """
        Gets the colleagues property value. Colleagues that are associated with this position.
        Returns: Optional[List[related_person.RelatedPerson]]
        """
        return self._colleagues
    
    @colleagues.setter
    def colleagues(self,value: Optional[List[related_person.RelatedPerson]] = None) -> None:
        """
        Sets the colleagues property value. Colleagues that are associated with this position.
        Args:
            value: Value to set for the colleagues property.
        """
        self._colleagues = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WorkPosition and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.workPosition"
        # Categories that the user has associated with this position.
        self._categories: Optional[List[str]] = None
        # Colleagues that are associated with this position.
        self._colleagues: Optional[List[related_person.RelatedPerson]] = None
        # The detail property
        self._detail: Optional[position_detail.PositionDetail] = None
        # Denotes whether or not the position is current.
        self._is_current: Optional[bool] = None
        # Contains detail of the user's manager in this position.
        self._manager: Optional[related_person.RelatedPerson] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkPosition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkPosition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkPosition()
    
    @property
    def detail(self,) -> Optional[position_detail.PositionDetail]:
        """
        Gets the detail property value. The detail property
        Returns: Optional[position_detail.PositionDetail]
        """
        return self._detail
    
    @detail.setter
    def detail(self,value: Optional[position_detail.PositionDetail] = None) -> None:
        """
        Sets the detail property value. The detail property
        Args:
            value: Value to set for the detail property.
        """
        self._detail = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "colleagues": lambda n : setattr(self, 'colleagues', n.get_collection_of_object_values(related_person.RelatedPerson)),
            "detail": lambda n : setattr(self, 'detail', n.get_object_value(position_detail.PositionDetail)),
            "is_current": lambda n : setattr(self, 'is_current', n.get_bool_value()),
            "manager": lambda n : setattr(self, 'manager', n.get_object_value(related_person.RelatedPerson)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_current(self,) -> Optional[bool]:
        """
        Gets the isCurrent property value. Denotes whether or not the position is current.
        Returns: Optional[bool]
        """
        return self._is_current
    
    @is_current.setter
    def is_current(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCurrent property value. Denotes whether or not the position is current.
        Args:
            value: Value to set for the isCurrent property.
        """
        self._is_current = value
    
    @property
    def manager(self,) -> Optional[related_person.RelatedPerson]:
        """
        Gets the manager property value. Contains detail of the user's manager in this position.
        Returns: Optional[related_person.RelatedPerson]
        """
        return self._manager
    
    @manager.setter
    def manager(self,value: Optional[related_person.RelatedPerson] = None) -> None:
        """
        Sets the manager property value. Contains detail of the user's manager in this position.
        Args:
            value: Value to set for the manager property.
        """
        self._manager = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_collection_of_object_values("colleagues", self.colleagues)
        writer.write_object_value("detail", self.detail)
        writer.write_bool_value("isCurrent", self.is_current)
        writer.write_object_value("manager", self.manager)
    

