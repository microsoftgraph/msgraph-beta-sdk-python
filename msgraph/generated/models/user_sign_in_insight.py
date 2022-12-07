from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

governance_insight = lazy_import('msgraph.generated.models.governance_insight')

class UserSignInInsight(governance_insight.GovernanceInsight):
    def __init__(self,) -> None:
        """
        Instantiates a new UserSignInInsight and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.userSignInInsight"
        # Indicates when the user last signed in
        self._last_sign_in_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserSignInInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserSignInInsight
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserSignInInsight()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_sign_in_date_time": lambda n : setattr(self, 'last_sign_in_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_sign_in_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSignInDateTime property value. Indicates when the user last signed in
        Returns: Optional[datetime]
        """
        return self._last_sign_in_date_time
    
    @last_sign_in_date_time.setter
    def last_sign_in_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSignInDateTime property value. Indicates when the user last signed in
        Args:
            value: Value to set for the lastSignInDateTime property.
        """
        self._last_sign_in_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("lastSignInDateTime", self.last_sign_in_date_time)
    

