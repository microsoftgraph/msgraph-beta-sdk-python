from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

case_operation = lazy_import('msgraph.generated.models.ediscovery.case_operation')
source_collection = lazy_import('msgraph.generated.models.ediscovery.source_collection')

class EstimateStatisticsOperation(case_operation.CaseOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new estimateStatisticsOperation and sets the default values.
        """
        super().__init__()
        # The estimated count of items for the sourceCollection that matched the content query.
        self._indexed_item_count: Optional[int] = None
        # The estimated size of items for the sourceCollection that matched the content query.
        self._indexed_items_size: Optional[int] = None
        # The number of mailboxes that had search hits.
        self._mailbox_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The number of mailboxes that had search hits.
        self._site_count: Optional[int] = None
        # eDiscovery collection, commonly known as a search.
        self._source_collection: Optional[source_collection.SourceCollection] = None
        # The estimated count of unindexed items for the collection.
        self._unindexed_item_count: Optional[int] = None
        # The estimated size of unindexed items for the collection.
        self._unindexed_items_size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EstimateStatisticsOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EstimateStatisticsOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EstimateStatisticsOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "indexed_item_count": lambda n : setattr(self, 'indexed_item_count', n.get_int_value()),
            "indexed_items_size": lambda n : setattr(self, 'indexed_items_size', n.get_int_value()),
            "mailbox_count": lambda n : setattr(self, 'mailbox_count', n.get_int_value()),
            "site_count": lambda n : setattr(self, 'site_count', n.get_int_value()),
            "source_collection": lambda n : setattr(self, 'source_collection', n.get_object_value(source_collection.SourceCollection)),
            "unindexed_item_count": lambda n : setattr(self, 'unindexed_item_count', n.get_int_value()),
            "unindexed_items_size": lambda n : setattr(self, 'unindexed_items_size', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def indexed_item_count(self,) -> Optional[int]:
        """
        Gets the indexedItemCount property value. The estimated count of items for the sourceCollection that matched the content query.
        Returns: Optional[int]
        """
        return self._indexed_item_count
    
    @indexed_item_count.setter
    def indexed_item_count(self,value: Optional[int] = None) -> None:
        """
        Sets the indexedItemCount property value. The estimated count of items for the sourceCollection that matched the content query.
        Args:
            value: Value to set for the indexedItemCount property.
        """
        self._indexed_item_count = value
    
    @property
    def indexed_items_size(self,) -> Optional[int]:
        """
        Gets the indexedItemsSize property value. The estimated size of items for the sourceCollection that matched the content query.
        Returns: Optional[int]
        """
        return self._indexed_items_size
    
    @indexed_items_size.setter
    def indexed_items_size(self,value: Optional[int] = None) -> None:
        """
        Sets the indexedItemsSize property value. The estimated size of items for the sourceCollection that matched the content query.
        Args:
            value: Value to set for the indexedItemsSize property.
        """
        self._indexed_items_size = value
    
    @property
    def mailbox_count(self,) -> Optional[int]:
        """
        Gets the mailboxCount property value. The number of mailboxes that had search hits.
        Returns: Optional[int]
        """
        return self._mailbox_count
    
    @mailbox_count.setter
    def mailbox_count(self,value: Optional[int] = None) -> None:
        """
        Sets the mailboxCount property value. The number of mailboxes that had search hits.
        Args:
            value: Value to set for the mailboxCount property.
        """
        self._mailbox_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("indexedItemCount", self.indexed_item_count)
        writer.write_int_value("indexedItemsSize", self.indexed_items_size)
        writer.write_int_value("mailboxCount", self.mailbox_count)
        writer.write_int_value("siteCount", self.site_count)
        writer.write_object_value("sourceCollection", self.source_collection)
        writer.write_int_value("unindexedItemCount", self.unindexed_item_count)
        writer.write_int_value("unindexedItemsSize", self.unindexed_items_size)
    
    @property
    def site_count(self,) -> Optional[int]:
        """
        Gets the siteCount property value. The number of mailboxes that had search hits.
        Returns: Optional[int]
        """
        return self._site_count
    
    @site_count.setter
    def site_count(self,value: Optional[int] = None) -> None:
        """
        Sets the siteCount property value. The number of mailboxes that had search hits.
        Args:
            value: Value to set for the siteCount property.
        """
        self._site_count = value
    
    @property
    def source_collection(self,) -> Optional[source_collection.SourceCollection]:
        """
        Gets the sourceCollection property value. eDiscovery collection, commonly known as a search.
        Returns: Optional[source_collection.SourceCollection]
        """
        return self._source_collection
    
    @source_collection.setter
    def source_collection(self,value: Optional[source_collection.SourceCollection] = None) -> None:
        """
        Sets the sourceCollection property value. eDiscovery collection, commonly known as a search.
        Args:
            value: Value to set for the sourceCollection property.
        """
        self._source_collection = value
    
    @property
    def unindexed_item_count(self,) -> Optional[int]:
        """
        Gets the unindexedItemCount property value. The estimated count of unindexed items for the collection.
        Returns: Optional[int]
        """
        return self._unindexed_item_count
    
    @unindexed_item_count.setter
    def unindexed_item_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unindexedItemCount property value. The estimated count of unindexed items for the collection.
        Args:
            value: Value to set for the unindexedItemCount property.
        """
        self._unindexed_item_count = value
    
    @property
    def unindexed_items_size(self,) -> Optional[int]:
        """
        Gets the unindexedItemsSize property value. The estimated size of unindexed items for the collection.
        Returns: Optional[int]
        """
        return self._unindexed_items_size
    
    @unindexed_items_size.setter
    def unindexed_items_size(self,value: Optional[int] = None) -> None:
        """
        Sets the unindexedItemsSize property value. The estimated size of unindexed items for the collection.
        Args:
            value: Value to set for the unindexedItemsSize property.
        """
        self._unindexed_items_size = value
    

