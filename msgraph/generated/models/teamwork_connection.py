from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_connection_status = lazy_import('msgraph.generated.models.teamwork_connection_status')

class TeamworkConnection(AdditionalDataHolder, Parsable):
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
    def connection_status(self,) -> Optional[teamwork_connection_status.TeamworkConnectionStatus]:
        """
        Gets the connectionStatus property value. Indicates whether a component/peripheral is connected/disconnected or its state is unknown. The possible values are: unknown, connected, disconnected, unknownFutureValue.
        Returns: Optional[teamwork_connection_status.TeamworkConnectionStatus]
        """
        return self._connection_status
    
    @connection_status.setter
    def connection_status(self,value: Optional[teamwork_connection_status.TeamworkConnectionStatus] = None) -> None:
        """
        Sets the connectionStatus property value. Indicates whether a component/peripheral is connected/disconnected or its state is unknown. The possible values are: unknown, connected, disconnected, unknownFutureValue.
        Args:
            value: Value to set for the connectionStatus property.
        """
        self._connection_status = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkConnection and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether a component/peripheral is connected/disconnected or its state is unknown. The possible values are: unknown, connected, disconnected, unknownFutureValue.
        self._connection_status: Optional[teamwork_connection_status.TeamworkConnectionStatus] = None
        # Time at which the state was last changed. For example, indicates connected since when the state is connected and disconnected since when the state is disconnected.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkConnection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkConnection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connection_status": lambda n : setattr(self, 'connection_status', n.get_enum_value(teamwork_connection_status.TeamworkConnectionStatus)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Time at which the state was last changed. For example, indicates connected since when the state is connected and disconnected since when the state is disconnected.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Time at which the state was last changed. For example, indicates connected since when the state is connected and disconnected since when the state is disconnected.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
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
        writer.write_enum_value("connectionStatus", self.connection_status)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

