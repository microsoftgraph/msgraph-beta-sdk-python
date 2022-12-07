from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class GovernanceInsight(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new governanceInsight and sets the default values.
        """
        super().__init__()
        # Indicates when the insight was created.
        self._insight_created_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GovernanceInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceInsight
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GovernanceInsight()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "insight_created_date_time": lambda n : setattr(self, 'insight_created_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def insight_created_date_time(self,) -> Optional[datetime]:
        """
        Gets the insightCreatedDateTime property value. Indicates when the insight was created.
        Returns: Optional[datetime]
        """
        return self._insight_created_date_time
    
    @insight_created_date_time.setter
    def insight_created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the insightCreatedDateTime property value. Indicates when the insight was created.
        Args:
            value: Value to set for the insightCreatedDateTime property.
        """
        self._insight_created_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("insightCreatedDateTime", self.insight_created_date_time)
    

