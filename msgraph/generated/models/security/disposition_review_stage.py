from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class DispositionReviewStage(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new dispositionReviewStage and sets the default values.
        """
        super().__init__()
        # Name representing each stage within a collection.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A collection of reviewers at each stage.
        self._reviewers_email_addresses: Optional[List[str]] = None
        # The sequence number for each stage of the disposition review.
        self._stage_number: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DispositionReviewStage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DispositionReviewStage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DispositionReviewStage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "reviewers_email_addresses": lambda n : setattr(self, 'reviewers_email_addresses', n.get_collection_of_primitive_values(str)),
            "stage_number": lambda n : setattr(self, 'stage_number', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name representing each stage within a collection.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name representing each stage within a collection.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def reviewers_email_addresses(self,) -> Optional[List[str]]:
        """
        Gets the reviewersEmailAddresses property value. A collection of reviewers at each stage.
        Returns: Optional[List[str]]
        """
        return self._reviewers_email_addresses
    
    @reviewers_email_addresses.setter
    def reviewers_email_addresses(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the reviewersEmailAddresses property value. A collection of reviewers at each stage.
        Args:
            value: Value to set for the reviewersEmailAddresses property.
        """
        self._reviewers_email_addresses = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("reviewersEmailAddresses", self.reviewers_email_addresses)
        writer.write_int_value("stageNumber", self.stage_number)
    
    @property
    def stage_number(self,) -> Optional[int]:
        """
        Gets the stageNumber property value. The sequence number for each stage of the disposition review.
        Returns: Optional[int]
        """
        return self._stage_number
    
    @stage_number.setter
    def stage_number(self,value: Optional[int] = None) -> None:
        """
        Sets the stageNumber property value. The sequence number for each stage of the disposition review.
        Args:
            value: Value to set for the stageNumber property.
        """
        self._stage_number = value
    

